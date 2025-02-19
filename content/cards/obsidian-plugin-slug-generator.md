---
title: 写一个obsidian插件 自动生成slug
date created: 2024-05-29 17:11
date modified: 2024-08-16 11:50
slug: obsidian-plugin-slug-generator
tags:
  - Area/PKM/Obsidian
---
 

参考
https://docs.obsidian.md/Plugins/Editor/Communicating+with+editor+extensions


我想做一个obsidian插件，它的功能：
当用户执行命令“slug generate” 
1. 获取当前打开文件的文档属性
2. 获取当前打开文件的标题
3. 将标题内容放到文档属性 slug 字段，如果没有拿到 文档属性，就
4. 将修改后的文档属性保存回当前打开文件


请帮我完善下列代码块

```
		this.addCommand({
			id: 'slug-generate-editor-command',
			name: 'slug generate',
			editorCallback: (editor: Editor, view: MarkdownView) => {
				console.log(editor.getValue());
				console.log(editor.getSelection());
				editor.replaceSelection('Sample Editor 1 Command');
			}
		});
```
