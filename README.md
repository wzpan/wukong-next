# wukong-next

Next 课堂版本的 wukong-robot 。可用于查看每一阶段编写的代码。

## 更新进度

目前只完成到 P2 第五章。更多的章节等后面有空再补上（作者太忙了……）。

## 如何查看历史某个阶段的代码

想看某一节的代码，可以到[历史页](https://github.com/wzpan/wukong-next/commits/master) 找到对应节的 commit id （也可以直接在本地使用 `git log` 命令查看和查找历史提交）。例如 P2 4.6 就是 f797b08 。然后在本地 `git checkout <commit-id>` 即可切换到那个阶段的代码。例如 `git checkout f797b08` 就会切换到 P2 4.6 时候写的代码。等想切回最新代码，可以使用 `git checkout master`。





