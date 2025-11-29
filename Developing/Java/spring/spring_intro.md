# spring

## spring介绍

### Spring 模块介绍

1. 核心容器
    核心容器：Spring-beans 和 Spring-core 模块是 Spring 框架的核心模块，包含控制反转（Inversion of Control, IoC）和依赖注入（Dependency Injection, DI）,核心容器提供 Spring 框架的基本功能。核心容器的主要组件是 BeanFactory，工厂模式的实现。BeanFactory 使用控制反转（IOC） 思想将应用程序的配置和依赖性规范与实际的应用程序代码分开。
2. Spring-AOP
    Spring-AOP是Spring的另一个核心模块, 在Spring中，他是以JVM的动态代理技术为基础，然后设计出了一系列的Aop横切实现，比如前置通知、返回通知、异常通知等。通过其配置管理特性，Spring AOP 模块直接将面向切面的编程功能集成到了 Spring 框架中。所以，可以很容易地使 Spring 框架管理的任何对象支持 AOP。
3. Spring Data Access(数据访问)
    由Spring-jdbc、Spring-tx、Spring-orm、Spring-jms和Spring-oxm 5个模块组成 。
4. Web 模块
    由Spring-web、Spring-webmvc、Spring-websocket和Spring-webmvc-portlet 4个模块组成，Web 上下文模块建立在应用程序上下文模块之上，为基于 Web 的应用程序提供了上下文。Web 模块还简化了处理多部分请求以及将请求参数绑定到域对象的工作。（这部分就是学习SpringMVC，这里可以看出，Springmvc是包含于spring的框架。）
5. 报文发送
    Spring-messaging是Spring4新加入的一个模块，主要职责是为Spring 框架集成一些基础的报文传送应用。
6. 单元测试

### IoC/DI

#### 概念

IOC/DI属于同一件事情的两个名称，一定注意，是一个事，不是两个事。
IoC/DI是指一个过程：创建对象的权利，或者是控制的位置，由JAVA代码转移到spring容器，由spring的容器控制对象的创建，就是控制反转，spring创建对象时，会读取配置文件中的信息，然后使用反射给我们创建好对象之后在容器（其实就是一个map集合）中存储起来，当我们需要某个对象时，通过id获取对象即可，不需要我们自己去new。

#### 好处

Spring IoC/DI使用后可以管理项目中相关对象，让对象管理的事情和业务分离（解耦）。同时程序员也不管理对象的依赖关系，所有的依赖关系交给Spring容器进行管理。

以后如果改变实现类，只需要修改配置文件即可，不需要去java代码中操作了。
要注意我们改都是改实现类，不会改接口，接口是规范，就像灯坏了我们一般换灯泡，不会把灯拆了。

## 容器 Bean 对象实例化模拟

在不依赖spring的情况下，自己模拟bean对象实例化的过程。

1. 定义xml文件，里面定义bean标签，因为后续每个bean标签会被解析为一个对象
2. 解析xml文件(dom4j)，解析的时候，会解析xml文件中的bean标签，每个bean标签转换为一个bean对象，此对象包含两个属性：id、class，此对象用来存放bean的id和class值。
3. 因为xml文件中bean标签可能是多个，所以定义一个List集合，存储bean对象。
4. 遍历List集合，得到每一个bean对象，通过bean对象的class属性，反射创建对应的对象。
5. 对象创建好以后，将bean对象的id和反射创建的对象，放入map集合中。
6. 定义一个工厂，（2）-（5）步骤放在工厂的构造器中完成。
7. 工厂中定义获取对象的方法，通过id从map集合中获取对象。

## spring 使用

### 自动注入

在Spring中，允许Bean的自动注入。有两种方式进行配置：default-autowire和autowire,底层也是基于构造注入或者设置注入的。

* 在根标签`<bean>`中配置autowire属性，此标签代表整个Spring中自动注入的策略。autowire属性取值有5个。

  default:默认值。不自动注入。

  no：不自动注入。

  byName:通过名称自动注入。会自动寻找容器中id的名字 与当前属性同名的bean进行注入。（底层调用的是setter方法）

  byType：通过类型自动注入。会自动寻找容器中bean的类型  与当前bean类型匹配的bean进行注入。如果有多个相同类型的bean注入会出现异常。（底层调用的是setter方法）

  constructor:通过构造方法进行注入。寻找bean的构造方法中是否有合适的构造器。如果有自动注入进去。类型先byType后byName，如果没找到不注入。注：构造方法类型和其他Bean的类型相同。（底层调用的是构造器）

### spring bean

#### 注意点

**（1）lazy-init属性（懒加载）**
    如果为false，则在IOC容器启动时会实例化bean对象，默认false
    如果为true，则IOC容器启动时不会实例化Bean对象，在使用bean对象时才会实例化

**（2）lazy-init设置为false有什么好处？**
    1）可以提前发现潜在的配置问题
    2）Bean 对象存在于缓存中，使用时不用再去实例化bean，加快程序运行效率

**（3）Spring 中 Bean是否是线程安全的**？
​   如果bean的scope是单例的，bean不是线程安全的。
​   如果bean的scope是prototype，bean是线程安全的。

**（4）什么对象适合作为单例对象？**
    一般来说对于无状态或状态不可改变的对象适合使用单例模式。（不存在会改变对象状态的成员变量）
    比如：controller层、service层、dao层

**（5）什么是无状态或状态不可改变的对象？**
    实际上对象状态的变化往往均是由于属性值得变化而引起的，比如user类 姓名属性会有变化，属性姓名的变化一般会引起user对象状态的变化。对于我们的程序来说，无状态对象没有实例变量的存在，保证了线程的安全性，service 层业务对象即是无状态对象。线程安全的。

#### 生命周期

Spring容器管理的bean也存在生命周期的概念，在Spring中，Bean的生命周期包括Bean的定义、初始化、使用和销毁4个阶段。

1. Bean 的初始化
    默认在IOC容器加载时，实例化对象。初始化有两种方式：
   1. 在配置文档中通过指定 init-method 属性来完成。

   ```java
    public class Person {
        // 定义初始化时需要被调用的方法
        public void init() {
            System.out.println("Person init...");
        }
    }
    ```

    xml 配置

    ```xml
    <!-- 通过init-method属性指定方法 -->
    <bean id="p" class="com.clarence.spring.pojo.Person" init-method="init"></bean>
    ```

   2. 实现 org.springframework.beans.factory.InitializingBean 接口。

    ```java
    public class Person implements InitializingBean {

        @Override
        public void afterPropertiesSet() throws Exception {
            System.out.println("Person init...");
        }
    }
    ```

    ```xml
    <bean id="p" class="com.clarence.pojo.Person" ></bean>
    ```

2. Bean 的使用

    ```java
    // 得到Spring的上下文环境
    BeanFactory factory = new ClassPathXmlApplicationContext("spring.xml");
    Person p = (Person) factory.getBean("Person");
    ```

3. Bean 的销毁
    配置destroy-method，通过 AbstractApplicationContext 对象，调用其close方法实现bean的销毁过程

