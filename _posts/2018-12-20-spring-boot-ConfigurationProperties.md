---
layout: article
title: SpringBoot 配置类读取自定义配置 + idea中自动补全
key: spring_boot_ConfigurationProperties_idea
tags:
  SpringBoot
  Idea
---
Config类读取自定义配置，为idea中编辑配置文件设置自动补全。
<!--more-->

## 自定义配置
使用 @ConfigurationProperties(perfix = "elasticsearch") 注解Config类，  
Config类中的属性会根据注解中的指定的前缀去找application.yml中查找，并自动读入到Config类中。

如配置类ElasticSearchConfig.java 需要从配置文件读取host、port属性
```java
import lombok.Setter;
import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.context.annotation.Configuration;

@Setter
@Configuration
@ConfigurationProperties(prefix = "spring.elasticsearch")
public class ElasticSearchConfig {
    private String host;

    private Integer port;

    ...  
}
```
注意每个要获取配置值的属性都要有setter。  
@Setter注解是为了少写Setter。具体请看[这篇博客](/2018/12/19/idea_lombok_annotation.html)

application.yml应该这样写
```yml
spring:
  elasticsearch:
    host: XXX.XXX.XXX.XXX
    port: 9300
```

还要在你的Application启动类里加上注解EnableConfigurationProperties，允许读配置文件
```java
import org.springframework.boot.context.properties.EnableConfigurationProperties;

@SpringBootApplication
@EnableConfigurationProperties // <- 新加的
public class DemoApplication {

    public static void main(String[] args) {
        SpringApplication.run(DemoApplication.class, args);
    }
}
```

## 自定义配置 idea自动补全
没有自动补全，万一打错key 或者 value类型不对就尴尬了

### 依赖
pom.xml
```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-configuration-processor</artifactId>
    <optional>true</optional>
</dependency>
```
### 加注解
ElasticSearchConfig.java
```java
import org.springframework.boot.context.properties.EnableConfigurationProperties;

@Setter
@Configuration
@ConfigurationProperties(prefix = "spring.elasticsearch")
@EnableConfigurationProperties(ElasticSearchConfig.class)  // <- 新加的
public class ElasticSearchConfig {
  ...
}
```

### 效果
重新编译
```
mvn clean
mvn install
```
会生成target/classes/META-INF/spring-configuration-metadata.json

现在编辑配置文件，可以发现自定义的配置已经有代码补全了
![](/assets/photo/20181220-code-completion-custom-properties.png)

## 完整代码

// todo

## thanks
[原博客链接http://www.mdoninger.de/2015/05/16/completion-for-custom-properties-in-spring-boot.html](http://www.mdoninger.de/2015/05/16/completion-for-custom-properties-in-spring-boot.html)

