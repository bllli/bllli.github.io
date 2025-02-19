---
title: Java DTO, Data Transfer Object
date created: 2024-09-03 10:50
date modified: 2024-09-03 17:04
slug: java-dto-data-transfer-object
tags:
  - Area/RD/Java
---


see: https://saranganjana.medium.com/data-transfer-object-dto-in-java-66c4f3075362

```java
public class CustomerDTO {
  private final String firstName;
  private final String lastName;
  private final String email;
  public CustomerDTO(String firstName, String lastName, String email) {
    this.firstName = firstName;
    this.lastName = lastName;
    this.email = email;
  }
  public String getFirstName() {
    return firstName;
  }
  public String getLastName() {
    return lastName;
  }
  public String getEmail() {
    return email;
  }
}
```