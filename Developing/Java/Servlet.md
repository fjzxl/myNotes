# Servlet

## 父子modules构建

### 父项目

先创建一个no-Archtype的maven项目，删除src和lib文件夹，修改pom.xml，作为父module，主要修改packaging为pom

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.clarence.servlet</groupId>
    <artifactId>parent</artifactId>
    <version>1.0。0</version>
    <packaging>pom</packaging>

    <properties>
        <maven.compiler.source>21</maven.compiler.source>
        <maven.compiler.target>21</maven.compiler.target>
    </properties>

</project>
```

### 子项目

创建一个maven-archetype-webapp项目，路径选则父目录下。

最后两个pom，父pom

```xml
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
      
  <modelVersion>4.0.0</modelVersion>
      
  <groupId>com.clarence.servlet</groupId>
      
  <artifactId>parent</artifactId>
      
  <version>1.0.0</version>
      
  <packaging>pom</packaging>
      
  <properties>
            
    <maven.compiler.source>21</maven.compiler.source>
            
    <maven.compiler.target>21</maven.compiler.target>
        
  </properties>
  
  <modules>
      
    <module>demo01</module>
      
  </modules>

  
  
</project>

```

子pom

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>

  <parent>
    <artifactId>parent</artifactId>
    <groupId>com.clarence.servlet</groupId>
    <version>1.0.0</version>
  </parent>

  <groupId>com.example.xxx</groupId>
  <artifactId>demo01</artifactId>
  <version>1.0.0</version>
  <packaging>war</packaging>

  <name>demo01 Maven Webapp</name>
  <!-- FIXME change it to the project's website -->
  <url>http://www.example.com</url>

  <properties>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    <maven.compiler.source>21</maven.compiler.source>
    <maven.compiler.target>21</maven.compiler.target>
  </properties>

  <dependencies>
    <dependency>
      <groupId>junit</groupId>
      <artifactId>junit</artifactId>
    </dependency>
  </dependencies>

  <build>
    <finalName>demo01</finalName>
    <pluginManagement><!-- lock down plugins versions to avoid using Maven defaults (may be moved to parent pom) -->
      <plugins>
        <plugin>
          <artifactId>maven-clean-plugin</artifactId>
        </plugin>
        <!-- see http://maven.apache.org/ref/current/maven-core/default-bindings.html#Plugin_bindings_for_war_packaging -->
        <plugin>
          <artifactId>maven-resources-plugin</artifactId>
        </plugin>
        <plugin>
          <artifactId>maven-compiler-plugin</artifactId>
        </plugin>
        <plugin>
          <artifactId>maven-surefire-plugin</artifactId>
        </plugin>
        <plugin>
          <artifactId>maven-war-plugin</artifactId>
        </plugin>
        <plugin>
          <artifactId>maven-install-plugin</artifactId>
        </plugin>
        <plugin>
          <artifactId>maven-deploy-plugin</artifactId>
        </plugin>
      </plugins>
    </pluginManagement>
  </build>
</project>
```

## 添加dependencies

在父module中添加dependencyManagement，为所有子module提供依赖管理。

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>junit</groupId>
            <artifactId>junit</artifactId>
            <version>4.11</version>
            <scope>test</scope>
        </dependency>

        <!-- Servlet -->
        <dependency>
            <groupId>javax.servlet</groupId>
            <artifactId>javax.servlet-api</artifactId>
            <version>${sevlet.version}</version>
            <scope>provided</scope>
        </dependency>
    
        <!-- JSP -->
        <dependency>
        <groupId>javax.servlet.jsp</groupId>
        <artifactId>jsp-api</artifactId>
        <version>${jsp.version}</version>
        <scope>provided</scope>
        </dependency>
    
        <!-- JSTL -->
        <dependency>
        <groupId>javax.servlet</groupId>
        <artifactId>jstl</artifactId>
        <version>${jstl.version}</version>
        <scope>runtime</scope>
        </dependency>
    </dependencies>
  </dependencyManagement>
```

说明：因为程序在运行时需要 Tomcat web 服务器，Tomcat 包含 servlet 和 jsp 的相关 jar 包，所以将 Servlet 和 JSP 依赖的 scope 设置为 provided，这样打包时就不包括。JSTL 依赖的用于 JSP 页面的 EL 表达式。

---

修改子module的pom，不再需要版本和scope设置

```xml
<dependencies>
    <dependency>
      <groupId>junit</groupId>
      <artifactId>junit</artifactId>
    </dependency>

    <!-- Servlet -->
    <dependency>
      <groupId>javax.servlet</groupId>
      <artifactId>javax.servlet-api</artifactId>
    </dependency>

    <!-- JSP -->
  <dependency>
    <groupId>javax.servlet.jsp</groupId>
    <artifactId>jsp-api</artifactId>
  </dependency>

  <!-- JSTL -->
  <dependency>
    <groupId>javax.servlet</groupId>
    <artifactId>jstl</artifactId>
  </dependency>

  </dependencies>
```

## 创建sevlet

1. maven-archetype-web 模板没有创建 src/main/java 文件夹

2. 在java文件夹下创建com.clarence.servlet.HelloServlet

3. 继承HttpServlet，实现相应方法

4. 设置注解，使用@WebServlet将一个继承于javax.servlet.http.HttpServlet 的类定义为Servlet组件。在Servlet3.0中 ， 可以使用@WebServlet注解将一个继承于javax.servlet.http.HttpServlet的类标注为可以处理用户请求的 Servlet。或者在web.xml中配置

  ```xml
  <servlet>
          <servlet-name>a</servlet-name>
          <servlet-class>com.msb.testservlet.Servlet04</servlet-class>
      </servlet>
      <servlet-mapping>
          <servlet-name>a</servlet-name>
          <url-pattern>/s04</url-pattern>
      </servlet-mapping>
  ```
  
5. 发布项目并启动服务

## Servlet的工作流程

通过浏览器f12可以清晰的看到整个请求过程

1. 通过请求头获知浏览器访问的是哪个主机
2. 再通过请求行获取访问的是哪个一个web应用
3. 再通过请求行中的请求路径获知访问的是哪个资源
4. 通过获取的资源路径在配置中匹配到真实的路径，
5. 服务器会创建servlet对象，（如果是第一次访问时，创建servlet实例，并调用init方法进行初始化操作）
6. 调用service（request， response），并会生成HttpServletRequest实现类对象和HttpServletResponse实现类对象，用来处理请求和响应
7. 调用service完毕后返回服务器 由服务器将response缓冲区的数据取出，以http响应的格式发送给浏览器

## Servlet的生命周期

Servlet没有 main()方法，不能独立运行，它的运行完全由 Servlet 引擎来控制和调度。 所谓生命周期，指的是 servlet 容器何时创建 servlet 实例、何时调用其方法进行请求的处理、 何时并销毁其实例的整个过程。

- **实例和初始化时机**
  当请求到达容器时，容器查找该 servlet 对象是否存在，如果不存在，则会创建实例（通过反射）并进行初始化。
- **就绪/调用/服务阶段**
  有请求到达容器，容器调用 servlet 对象的 service()方法,处理请求的方法在整个生命周期中可以被多次调用； HttpServlet 的 service()方法，会依据请求方式来调用 doGet()或者 doPost()方法。但是， 这两个 do 方法默认情况下，会抛出异常，需要子类去 override。
- **销毁时机**
  当容器关闭时（应用程序停止时），会将程序中的 Servlet 实例进行销毁。

上述的生命周期可以通过 Servlet 中的生命周期方法来观察。在 Servlet 中三个生命周期方法分别是**init**、**service**、**destroy**，不由用户手动调用，而是在特定的时机有容器自动调用，观察这三个生命周期方法 即可观察到 Servlet 的生命周期。

Servlet 的生命周期：
  ![Servlet生命周期](/Source/pics/developing/Java/Servlet/Servlet-lifecircle.png)

  1. Web Client 向 Servlet 容器（Tomcat）发出 Http 请求。
  2. Servlet 容器接收 Web Client 的请求。
  3. 根据反射构建Servlet对象（第一次请求会构建，之后不会重复创建对象，直到服务器关闭才会被销毁）
  4. 构建HttpServletRequest 实现类对象、HttpServletResponse 实现类对象 ，处理请求和响应
  5. Servlet 容器调Servlet对象的service方法，把HttpServletRequest 实现类对象与 HttpServletResponse 实现类对象作为service的参数，供给方法内部使用。
     1. Servlet 对象调用 HttpServletRequest 实现类对象的有关方法，获取 Http 请求信息
     2. Servlet 对象调用 HttpServletResponse实现类对象的有关方法，生成响应数据
     3. Servlet 容器把 Servlet对象的响应结果传给 Web Client

## HttpServletRequest对象

HttpServletRequest 对象：主要作用是用来接收客户端发送过来的请求信息，例如：请求的参数，发送的头信息等都属于客户端发来的信息，service()方法中形参接收的是 HttpServletRequest 接口的实例化对象，表示该对象主要应用在 HTTP 协议上，该对象是由 Tomcat 封装好传递过来。一切请求都围绕 HttpServletRequest 对象。该对象直接在 Service 方法中由容器传入过来，而我们需要做的就是取出对象中的数据，进行分析、处理。

### 常用方法

![请求常用方法](/Source/pics/developing/Java/Servlet/Servlet-requestmethod.png)

例子

```java
// 获取客户端请求的完整URL （从http开始，到?前面结束）
   String url = request.getRequestURL().toString();
   System.out.println("获取客户端请求的完整URL：" + url);
   //  获取客户端请求的部分URL （从站点名开始，到?前面结束）
   String uri = request.getRequestURI();
   System.out.println("获取客户端请求的部分URL：" + uri);
   // 获取请求行中的参数部分
   String queryString = request.getQueryString();
   System.out.println("获取请求行中的参数部分：" + queryString);
   // 获取客户端的请求方式
   String method = request.getMethod();
   System.out.println("获取客户端的请求方式：" + method);
   // 获取HTTP版本号
   String protocol = request.getProtocol();
   System.out.println("获取HTTP版本号：" + protocol);
   // 获取webapp名字 （站点名）
   String webapp = request.getContextPath();
   System.out.println("获取webapp名字：" + webapp);
```

### HttpServletRequest对象的使用

HttpServletRequest可以作为一个域对象（request域对象）使用，通过该对象可以在一个请求中传递数据，request 域对象中的数据在一次请求中有效，则经过请求转发，request 域中的数据依然存在，则在请求转发的过程中可以通过 request 来传输/共享数据。

例子

---

```Java
@WebServlet("/msb/sr03")
public class ServletRequest03 extends HttpServlet {
    @Override
    protected void service(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        // 获取前台传过来的数据：
        String uname = req.getParameter("uname");
        System.out.println("前台传到sr03-Servlet中的uname的数值为：" + uname);
        // 域对象数据的共享：
        req.setAttribute("age","18");
        String age = (String)req.getAttribute("age");
        System.out.println("servlet03---age:" + age);
        // 请求转发：
        req.getRequestDispatcher("/sr04").forward(req,resp);
        // 在请求转发以后输出一句话：
        System.out.println("-----sr03");
    }
}
```

---

```Java
@WebServlet("/sr04")
public class ServletRequest04 extends HttpServlet {
    @Override
    protected void service(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        // 获取请求数据：
        String uname = req.getParameter("uname");
        // 获取域对象中数据：
        String age = (String)req.getAttribute("age");
        System.out.println("servlet04---age:" + age);
        System.out.println("sr04-Servlet中获取uname的数值为：" + uname);
    }
}
```

### HttpServletResponse对象

Web服务器收到客户端的http请求，会针对每一次请求，分别创建一个用于**代表请求**的 request 对象和**代表响应**的 response 对象。
HttpServletResponse 的主要功能用于服务器对客户端的请求进行响应，将 Web 服务器处理后的结果返回给客户端。service()方法中形参接收的是 HttpServletResponse 接口的实例化对象，这个对象中封装了向客户端发送数据、发送响应头，发送响应状态码的方法。

### 乱码解决

```Java
// 设置请求信息的解码格式：
req.setCharacterEncoding("UTF-8");
// 设置响应信息的编码格式：
resp.setCharacterEncoding("UTF-8");
// 设置浏览器的编码格式：
resp.setContentType("text/html;charset=UTF-8");
```

### 请求转发与重定向的区别

**不同1：语法不同**
请求转发：request.getRequestDispatcher("dis02").forword(request,response);
重定向：response.sentRedirect("red02");

**不同2：请求不同**
请求转发：是一个请求
重定向：是不同的请求

**不同3：地址栏是否发生改变**
请求转发：不变
重定向：变

**不同4：请求参数能否携带**
请求转发：可以
重定向：不可以， 但是可以手动设置携带参数：resp.sendRedirect("red2?uname="+req.getParameter("uname")+"&pwd=123");

**不同5：执行效率不同**
请求转发：服务器内部跳转，所以效率高啊
重定向：相对效率低

**不同6：跳转范围不同**
请求转发：只能在服务器内部跳转
重定向：既能跳转服务器内部资源，又能跳转服务器外部资源

**不同7：表单是否发生重复提交**
请求转发：会，指的是数据提交后，刷新页面，因为地址栏地址不变，每刷新一次都会重复请求一次，数据提交一次。如果刚好是个添加操作，每次都会添加一次。

重定向：不会

**不同8：路径书写方式不同**
（1）绝对路径 - 有协议、IP、端口 ，eg: <http://www.baidu.com>

​  请求转发：不支持
​  重定向：支持

（2）相对路径：相对servlet的url地址的路径   (不建议)
  自行测试：将第一个servlet地址改为"/msb/s1",然后分别请求转发，重定向到第二个servlet，观看相对地址和运行结果
  对于不加/，就是相对路径，相对servlet配置的url-pattern(请求地址)，所以你要是url-pattern配置的是 /a  那么不加/ 没啥问题  ,但是url-pattern里面要是 /a/b/c  那么在访问jsp的时候 可能就出错了！  代码不加/就出错了！

（3）根路径： 资源路径加"/"    （建议）
  请求转发：到项目根目录下查找资源    <http://localhost:8080/项目访问名/>
  重定向：到服务器根目录下查找资源    <http://localhost:8080/>  
  eg:resp.sendRedirect(req.getContextPath()+"/dis2");

### 转发和重定向使用场景

1. 跳转前后是否需要共享request中数据
  如果需要共享：转发
  如果不需要共享：都可以
2. 是否要跳转到服务器外部资源
   如果需要跳出项目：重定向
   如果不需要:都可以
3. 是否涉及表单重复提交
  重定向：不会造成表单重复提交
  转发：会造成表单重复提交

