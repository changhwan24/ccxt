from socket_data.base.socket_data import socket_data
import time

class okex_data(socket_data):
    name = ""
    data = {}
    timestamp = int(round(time.time() * 1000))
    orderbooks = []

    def __init__(self, dic):
        self.name = dic['name']
        self.data = dic['data']


    def datamining(self):
        dic = {}

        print(self.data)

        # _data = self.data['data']        
        # self.set_orderbooks(self.name, _data)

        # # 제대로 되어 있는지 확인
        # for i in range(len(self.orderbooks)):
        #     print(self.orderbooks[i])

        return dic

    @classmethod
    def set_orderbooks(self, name, data):
        self.orderbooks = []

        exchange_type = "futures"
        exchange_name = name       

        lists = ["bids", "asks"]
        for i in range(len(lists)):
            kind = lists[i]
            _orderbooks = data[kind]

            for j in range(len(_orderbooks)):                
                orderbook = {}

                orderbook["exchange_type"] = exchange_type
                orderbook["exchange_name"] = name
                orderbook["symbol"] = "BTC/USD/SWAP"
                orderbook["kind"] = kind
                orderbook["id"] = j
                orderbook["timestamp"] = self.timestamp
                orderbook["price"] = _orderbooks[j][0]
                orderbook["volume"] = _orderbooks[j][1]

                self.orderbooks.append(orderbook)


    