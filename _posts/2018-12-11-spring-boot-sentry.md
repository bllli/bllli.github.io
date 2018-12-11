---
layout: article
title: SpringBoot集成Sentry异常收集
key: spring-boot-sentry
tags:
  java
  SpringBoot
---
SpringBoot集成Sentry，使用sentry-spring而非sentry-logback。完整代码示例。
<!--more-->

## 配置

### 引包
Maven:
```
<!--sentry-->
<dependency>
    <groupId>io.sentry</groupId>
    <artifactId>sentry-spring</artifactId>
    <version>1.7.16</version>
</dependency>
```

[其他包管理器](https://search.maven.org/artifact/io.sentry/sentry-spring/1.7.16/jar)

### 配置类
SentryConfig.java
```
import io.sentry.Sentry;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.web.servlet.ServletContextInitializer;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.HandlerExceptionResolver;

/**
 * Sentry 配置类
 * @author bllli
 */
@Configuration
public class SentryConfig {
    private static final Logger logger = LoggerFactory.getLogger(SentryConfig.class) ;

    @Value("${sentry_dsn}")
    private String sentryDSN;

    @Bean
    public HandlerExceptionResolver sentryExceptionResolver() {
        if (sentryDSN != null && !sentryDSN.isEmpty()) {
            // 初始化sentry
            Sentry.init(sentryDSN);
        } else {
            logger.error("sentry_dsn NOT CONFIG, errors will not send to your sentry server.");
        }
        return new io.sentry.spring.SentryExceptionResolver();
    }

    @Bean
    public ServletContextInitializer sentryServletContextInitializer() {
        return new io.sentry.spring.SentryServletContextInitializer();
    }
}
```

确保配置类所在包能被ComponentScan扫到
```
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.ComponentScan;

@SpringBootApplication
@ComponentScan(basePackages = {
        "cn.bllli.demo.springbootsentry.config",  // <-- 这儿
        "cn.bllli.demo.springbootsentry.controllers",
})
public class SpringBootSentryApplication {

    public static void main(String[] args) {
        SpringApplication.run(SpringBootSentryApplication.class, args);
    }
}
```

### 配置DSN
推荐使用yml配置, 便于区分开发测试生产环境  
application.yml
```
spring:
  profiles:
    active: local

---
# 本地
spring:
  profiles: local

sentry_dsn: # todo: add your local dsn

---
# 测试环境
spring:
  profiles: test

sentry_dsn: # todo: add your test dsn

---
# 生产环境
spring:
  profiles: prod

sentry_dsn: # todo: add your prod dsn
```

启动服务时指定启用的配置
```
java -jar <your-app-name>.jar --spring.profiles.active=dev
```

## 效果
发送请求
![](/assets/photo/20181211-div-get.png)

sentry接到异常
![](/assets/photo/20181211-div-zero-sentry.jpg)
## 完整代码
[https://github.com/bllli/spring-boot-sentry](https://github.com/bllli/spring-boot-sentry)

## Thanks
- [https://docs.sentry.io/clients/java/modules/spring/](https://docs.sentry.io/clients/java/modules/spring/)


