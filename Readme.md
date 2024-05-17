# 果宝特攻（FRUIT ROBO)

项目演示视频参考文件内“项目演示视频.mp4”

项目详情信息参考https://github.com/xuxu6022/FRUITYROBO

## 技术栈

### Vue3

Vue 3 是 Vue.js 的最新主要版本，带来了许多性能提升和新特性，旨在增强开发体验和应用效率。它通过重写虚拟 DOM 实现（使用 Proxy 代替 Object.defineProperty），显著提升了渲染性能和内存使用效率。Vue 3 引入了组合式 API（Composition API），提供了一种新的 API 设计模式，使代码更加可读和可重用，特别适合处理复杂组件。此外，Vue 3 从设计之初就考虑了对 TypeScript 的支持，提供了更友好的开发体验。新的组件生命周期钩子经过优化，新增了一些钩子，并改进了命名以提升直观性。Vue 3 还支持 Fragments，允许组件返回多个根节点，以及 Teleport，使得模板的一部分可以渲染到 DOM 的其他位置，适用于模态框和工具提示等 UI 元素。此外，它提供了简单的依赖注入机制，允许在组件树中注入和使用状态或方法。由 Vue 作者开发的前端构建工具 Vite 默认支持 Vue 3，提供了快速的冷启动和热模块替换体验。总之，Vue 3 通过这些改进成为一个更现代和高效的框架，适用于构建复杂的前端应用。更多信息和详细指南可以参考 [Vue 3 官方文档](https://v3.vuejs.org/)。

### element-plus

Element Plus 是一套基于 Vue 3 的前端 UI 组件库，旨在帮助开发者快速构建现代化的 Web 应用程序。它是对 Element UI 的升级版本，提供了更多功能和改进，同时保持了 Element UI 的简洁和易用性。Element Plus 提供了丰富的组件库，涵盖了各种常见的 UI 组件，如按钮、表单、表格、弹窗、导航菜单等，以及一些高级组件和工具，如日期选择器、滑块、分页器、消息提示、图标库等。这些组件都经过精心设计和优化，支持响应式布局，并提供了丰富的配置选项和自定义主题功能，使开发者可以根据项目需求轻松定制和扩展组件的外观和行为。Element Plus 还提供了完善的文档和示例，帮助开发者快速上手并有效地使用组件库，同时也支持国际化和多语言环境，使得 Element Plus 可以被广泛应用于各种类型的 Web 项目中，从企业级应用到个人网站都可以得到良好的支持和体验。

### flask

Flask 是一个轻量级的 Python Web 应用框架，由 Armin Ronacher 开发。它以简洁、灵活和易用为特点，被广泛应用于构建各种类型的 Web 应用程序，包括简单的静态网站、RESTful API 服务、企业级应用等。Flask 基于 Werkzeug WSGI 工具库和 Jinja2 模板引擎，提供了一套简单而强大的工具和组件，使得开发者能够快速地搭建并扩展 Web 应用。

Flask 的设计理念是“微框架”，它并不强制性地包含大量预设功能，而是通过扩展插件的方式来提供各种功能，从而保持了框架的轻量级和灵活性。开发者可以根据项目需求选择合适的插件来扩展 Flask，例如数据库 ORM（如 SQLAlchemy）、表单处理（如 WTForms）、用户认证（如 Flask-Login）、RESTful API 支持（如 Flask-RESTful）等等。

Flask 还具有良好的文档和社区支持，有着丰富的教程和示例，使得学习和使用 Flask 变得相对容易。由于其灵活性和可扩展性，Flask 成为了许多 Python 开发者首选的 Web 框架之一，尤其适用于中小型项目或需要快速原型开发的场景。同时，Flask 也与各种前端框架（如 Vue.js、React、Angular 等）很好地配合，使得开发现代化的 Web 应用变得更加便捷和高效。

### sqlite3

SQLite3 是一种嵌入式的关系型数据库管理系统（RDBMS），它是以 C 语言编写的，并且不需要独立的服务器进程或配置。SQLite3 的设计目标之一是提供一个轻量级、快速、可靠的数据库解决方案，适用于各种规模的应用程序，包括移动应用、桌面应用和小型 Web 应用等。

相比于传统的数据库系统（如 MySQL、PostgreSQL 等），SQLite3 的特点之一是它将整个数据库存储在一个单一的文件中，这使得它在部署和管理上更加简单和方便。开发者只需将 SQLite3 的库文件嵌入到应用中，即可使用 SQL 查询语言进行数据库操作，而无需额外的数据库服务器。

SQLite3 支持大部分标准的 SQL 查询语法，包括创建表、插入数据、更新数据、删除数据以及复杂的查询操作（如联合查询、子查询等）。它还支持事务处理和触发器，可以保证数据的一致性和完整性。

由于 SQLite3 是一种嵌入式数据库，它在处理小型数据集和轻量级应用时表现出色。然而，对于大规模数据处理和高并发访问的应用，SQLite3 的性能可能不如一些专用的数据库系统。因此，开发者在选择数据库时应根据项目的特点和需求进行权衡和选择。

## 项目概述

FRUIT ROBO项目主要为监测运维水果商店的销售采购情况。

### HomePage

- 导航栏：根据需要随时进行页面跳转；
- 公告展示：最新两个公告标题展示，点击跳转至公告详情页面；
- 商品展示：显示最新的商品基本信息（最多显示4个）；
- 按钮跳转：点击按钮跳转至对应页面；
- 采购信息：显示最新5条采购信息；
- 销售信息：显示最新5条销售信息；
- 评论信息：显示最新一条评论信息。

### AnnouncementPage

- 导航栏：根据需要随时进行页面跳转；

- 显示公告详情信息。

### ProductPage

- 导航栏：根据需要随时进行页面跳转；

- 商品显示：自动布局，实时更新；

- 商品增加：点击按钮，自行增加商品信息；
- 商品修改：针对已有商品信息进行修改；
- 商品删除：删除不需要的商品。

### PurchasePage

- 导航栏：根据需要随时进行页面跳转；

- 采购显示：显示全部采购信息；
- 采购增加：点击按钮，自行增加采购信息；
- 采购删除：删除不需要的采购。

### SalePage

- 导航栏：根据需要随时进行页面跳转；

- 销售显示：显示全部销售信息。

### CommentPage

- 导航栏：根据需要随时进行页面跳转；

- 评论显示：显示全部评论信息；
- 评论删除：删除不正当评论。

## 如何使用

### 后端

配置python环境

在/flask文件目录下

```shell
conda create -n web python=3.9
conda activate web
pip install -r requirements.txt
python init.py
python app.py
```

### 前端

在/vue文件目录下

运行

```shell
npm run serve
```

