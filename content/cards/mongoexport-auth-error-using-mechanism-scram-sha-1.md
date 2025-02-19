---
title: mongo shell AuthenticationFailed SCRAM-SHA-1
date created: 2024-09-20 17:52
date modified: 2024-09-20 17:54
slug: mongoexport-auth-error-using-mechanism-scram-sha-1
tags:
  - Area/RD/踩坑经验/mongo
---

https://stackoverflow.com/questions/68927857/mongoexport-auth-error-using-mechanism-scram-sha-1

```shell
➜  mongodb mongodump --uri 'mongodb://root:example@localhost:27017' --db patient_recruitment_local -o backup
2024-09-20T17:53:04.099+0800	Failed: can't create session: failed to connect to mongodb://root:example@localhost:27017: connection() error occurred during connection handshake: auth error: sasl conversation error: unable to authenticate using mechanism "SCRAM-SHA-1": (AuthenticationFailed) Authentication failed.
```

```shell
--authenticationDatabase=admin
```
