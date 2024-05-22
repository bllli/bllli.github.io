---
title: Docker 运维 配置与维护
slug: docker-operations-configuration-and-maintenance
date created: 2024-05-22 17:36
date modified: 2024-05-22 17:53
feed: show
blog: tech
date: 2024-05-21
---

- 镜像下载地址  [[docker-pull-image-using-china-mirror|Docker 拉取镜像 使用中国镜像站]]
- 确认 image 存储地址
	- 详见配置文件 文件目录 `/etc/docker/daemon.json`
	- 默认为 /var/lib/docker/
	- 云服务厂商启动盘一般只给40G, 如果用默认地址容易占满
	- 如果有算法镜像起码200G，算法镜像一个就20多G 甚至50G，完全搞不懂怎么这么大
	- 修改存储地址 [how to change docker root data directory](https://tienbm90.medium.com/how-to-change-docker-root-data-directory-89a39be1a70b)
- 确认 volumn 存储地址
	- [How to change Docker storage location - Dmytro Kryvokhyzha](https://evodify.com/change-docker-storage-location/#:~:text=Edit%20the%20%2Fetc%2Fdefault%2Fdocker%20file%20by%20adding%20the%20new,should%20use%20%2Fmnt%2Fnewlocation%20as%20a%20new%20storage%20location.)



## snap 安装的 docker

/var/snap/docker/current/config/daemon.json
```
{
    "registry-mirrors": ["https://docker.nju.edu.cn/"]
}
```

```
sudo snap restart docker
```

### 维护

```sh
docker system prune
```
