from vnpy_ctastrategy import (
    CtaTemplate,
    StopOrder,
    TickData,
    BarData,
    TradeData,
    OrderData,
    BarGenerator,
    ArrayManager,
)

from vnpy.trader.constant import Interval

from vnpy_ctastrategy.base import Offset
# from vnpyExtend.extendArrayManager_walter import ExtendArrayManager
from vnpyExtend.extendArrayManager import ExtendArrayManager
from vnpyExtend.extendBarGenerator import ExtendBarGenerator
from vnpyExtend.extendCtaTemplate import ExtendCtaTemplate


class IntraDayStrategy(ExtendCtaTemplate):
    """
    创建时间:{{_date_}}
    作者: {{_author_}}, {{_email_}}
    策略名称:中文/English
    交易逻辑:
    """
    author = '{{_author_}}'

    {{_cursor_}}
    parameters = []
    variables = []

    def __init__(self, cta_engine, strategy_name, vt_symbol, setting):
        """"""
        super().__init__(cta_engine, strategy_name, vt_symbol, setting)

        self.bg5 = ExtendBarGenerator(self.on_bar, window=5, on_window_bar=self.on_5min_bar, interval=Interval.MINUTE)
        self.am5 = ExtendArrayManager(size=300)
        self.am5_heikin = ExtendArrayManager(size=300)

        self.bg1Hr = ExtendBarGenerator(self.on_bar, window=2, on_window_bar=self.on_hr_bar, interval=Interval.HOUR)
        self.am1Hr = ExtendArrayManager(size=50)
        self.am1Hr_heikin = ExtendArrayManager(size=50)

    def on_init(self):
        """
        Callback when strategy is inited.
        """
        self.write_log("策略初始化")
        self.load_bar(20)  # 5天

    def on_start(self):
        """
        Callback when strategy is started.
        """
        self.write_log("策略启动")

    def on_stop(self):
        """
        Callback when strategy is stopped.
        """
        self.write_log("策略停止")

    def on_tick(self, tick: TickData):
        """
        Callback of new tick data update.
        """
        self.bg5.update_tick(tick)
        self.bg1Hr.update_bar(tick)

    def on_bar(self, bar: BarData):
        """
        Callback of new bar data update.
        """
        self.bg5.update_bar(bar)
        self.bg1Hr.update_bar(bar)

    def on_5min_bar(self, bar: BarData):
        """"""
        self.cancel_all()

        self.am5.update_bar(bar)
        heikinBar = self.heikin_ashi(bar)
        self.am5_heikin.update_bar(heikinBar)

        if not self.am5.inited:
            return

        self.put_event()

    def _trading(self, bar: BarData, heikinBar: BarData):

        data = {
            'gateway_name': bar.gateway_name,
            'extra': bar.extra,
            'symbol': bar.symbol,
            'exchange': bar.exchange.value,
            'datetime': bar.datetime,
            'interval': bar.interval,
            'open_price': bar.open_price,
            'high_price': bar.high_price,
            'low_price': bar.low_price,
            'close_price': bar.close_price,
            'volume': bar.volume,
            # 'candle': {
            #     'boll_up_hr': boll_up_hr, 'boll_lo_hr': boll_low_hr, 'mid_hr': boll_mid_hr,
            #     'boll_up_min': boll_up_min, 'boll_lo_min': boll_up_min, 'mid_min': boll_low_min,
            #     'emaHr': ema_hr[-1], 'buy': buy},
            # 'rsiSma': {'rsi': rsi_hr, 'sma': sma_hr},
            # 'adx': {'adx': adx[-1], 'angle': adx_angle, 'slope': adx_slope},
        }

        self.draw_to_db(data)

    def on_hr_bar(self, bar: BarData):
        """"""
        self.am1Hr.update_bar(bar)
        heikinBar = self.heikin_ashi(bar)
        self.am1Hr_heikin.update_bar(heikinBar)

        if not self.am1Hr.inited:
            return

        self._trading(bar, heikinBar)
        self.put_event()

    def on_order(self, order: OrderData):
        """
        Callback of new order data update.
        """
        pass

    def on_trade(self, trade: TradeData):
        """
        Callback of new trade data update.
        """
        if trade.offset == Offset.CLOSE and self.pos == 0:
            self.cancel_all()
        trade.comment = self.orderComment.get(trade.vt_orderid)
        self.update_holding_cost(trade)
        self.trade_to_db(trade)
        self.put_event()

    def on_stop_order(self, stop_order: StopOrder):
        """
        Callback of stop order update.
        """
        pass
