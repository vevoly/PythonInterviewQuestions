# _*_ coding: utf-8 _*_
__author__ = 'jevoly'
__date__ = '2019/2/22 0022 下午 10:27'

"""
1 fanout
fanout类型的Exchange路由规则非常简单，它会把所有发送到
该Exchange的消息路由到所有鱼它绑定的Queue中。

生产者（P）生产消息1将消息1推送到Exchange，
由于Exchange Type=fanout这时候会遵循fanout的规则将消息
推送到所有与它绑定Queue，也就是图上的两个Queue最后两个消费者消费。

2 direct
direct类型的Exchange路由规则也很简单，它会把消息路由到那些
binding key与routing key完全匹配的Queue中。

当生产者（P）发送消息时Rotuing key=booking时，
这时候将消息传送给Exchange，Exchange获取到生产者发送过来消息后，
会根据自身的规则进行与匹配相应的Queue，这时发现Queue1和Queue2都
符合，就会将消息传送给这两个队列，
如果我们以Rotuing key=create和Rotuing key=confirm发送消息时，
这时消息只会被推送到Queue2队列中，其他Routing Key的消息将会被丢弃。

3 topic
direct是严格意义上的匹配，换言之Routing key必须与Binding key相匹配
的时候才将消息传送给Queue，那么topic这个规则就是模糊匹配，可以通过
通配符满足一部分规则就可以传送。
1） routing key为一个句点“.”分隔的字符，如"stock.usd.nyse"
2） binding key与routing key一样也是句点分隔的字符串。
3） binding key中可以存在两种特殊字符"*","#"，用于做模糊匹配，
其中*用于匹配一个单词，"#"用于匹配多个单词。

4 headers
headers类型的Exchange不依赖于routing key与binding key的匹配归来来路由消息，
而是根据发送消息内容中的headers属性进行匹配。
在绑定Queue与Exchange时制定一组键值对；当消息发送到Exchange时，RabbitMq会
取到该消息的headers（也是一个键值对的形式），对比其中的键值对是否完全匹配Queue与
Exchange绑定时制定的键值对；如果完全匹配则消息会路由到该Queue，否则不会路由到该Queue。


补充说明：
ConnectionFactory、Connection、Channel
ConnectionFactory、Connection、Channel都是RabbitMq对外提供的API中最基本的对象。
ConnectionFactory为Connection的制造工厂。
Channel是我们与RabbitMQ打交道的最重要的一个接口，我们大部分的业务操作是在Channel
这个接口中完成的，包括定义Queue、Exchange、绑定Queue与Exchange、发布消息等。
Connection就是建立以个TCP链接，生产者与消费者都是通过tcp链接到rabbitmq server中的。
Channel虚拟连接，建立在tcp链接的基础上，数据流动是通过channel来进行的。
"""