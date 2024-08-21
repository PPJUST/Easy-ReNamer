import os
from typing import Union

from PySide6.QtCore import Signal, QItemSelectionModel
from PySide6.QtGui import QDragEnterEvent, QPixmap, Qt
from PySide6.QtWidgets import QTableWidget, QHeaderView, QTableWidgetItem, QAbstractItemView, QMessageBox

from module import function_file_item, function_normal, WindowsSorted
from module.class_.class_rename_info import RenameInfo
from module.class_.class_rename_rule import RenameRule

_title_line = ['类型', '路径', '文件名', '预览', '进度']
_min_width = 30
_max_height = 16
_data_role = 1000


class TabWidgetFileList(QTableWidget):
    signal_drop_paths = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

        # 设置标题行
        self.setColumnCount(len(_title_line))
        self.setHorizontalHeaderLabels(_title_line)
        self.hideColumn(_title_line.index('路径'))  # 隐藏路径列，美观
        self.setColumnWidth(_title_line.index('类型'), _min_width)
        self.setColumnWidth(_title_line.index('进度'), _min_width)
        self.setColumnWidth(_title_line.index('文件名'), (378 - _min_width * 2) // 2)  # 固定大小时，控件的宽约为378
        self.setColumnWidth(_title_line.index('预览'), (378 - _min_width * 2) // 2)  # 固定大小时，控件的宽约为378

        # ui设置
        self.setAcceptDrops(True)
        self.setDragDropMode(self.DragDropMode.InternalMove)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)  # 选择模式为整行
        self.verticalHeader().setVisible(False)  # 不显示行号
        self.setVerticalScrollMode(QTableWidget.ScrollPerPixel)  # 平滑滚动
        self.setHorizontalScrollMode(QTableWidget.ScrollPerPixel)  # 平滑滚动
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)  # 手动调整列宽
        # self.setSortingEnabled(True)  # 设置排序
        self.horizontalHeader().sectionClicked.connect(self.sort_item)  # 修改排序方法

        # 初始化
        self._current_order = None  # 当前排序类型，None/ASC/DESC

    def sort_item(self, column: int):
        """排序行项目"""
        function_normal.print_function_info()
        if column == _title_line.index('文件名'):
            # 更新排序方法
            if self._current_order is None:
                self._current_order = 'ASC'
            elif self._current_order == 'ASC':
                self._current_order = 'DESC'
            elif self._current_order == 'DESC':
                self._current_order = 'ASC'
            else:
                self._current_order = 'ASC'
            # 冒泡排序（逐个上移/下移）
            n = self.rowCount()
            for i in range(n):
                for j in range(n - i - 1):
                    # 提取相邻两行的文件名，按排序规则进行排序后判断是否需要互换位置
                    filename_1 = self.item(j, _title_line.index('预览')).data(_data_role).filename_need
                    filename_2 = self.item(j + 1, _title_line.index('预览')).data(_data_role).filename_need
                    joined_list = [filename_1, filename_2]
                    sorted_list = WindowsSorted.sort_list(joined_list, self._current_order)
                    if joined_list != sorted_list:
                        self.change_item_position(j, j + 1)
            # 刷新预览文件名
            self.calc_new_filename()

    def insert_path_item(self, paths: Union[list, str]):
        """插入路径行项目"""
        function_normal.print_function_info()
        if isinstance(paths, str):
            paths = [paths]

        paths = [os.path.normpath(i) for i in paths]

        for path in paths:
            if path not in self.paths_showed():
                row_position = self.rowCount()
                self.insertRow(row_position)
                self.setRowHeight(row_position, _max_height)  # 固定行高
                # 插入图标
                pixmap = QPixmap()
                pixmap.loadFromData(function_file_item.get_icon_filetype(path))
                item_icon = QTableWidgetItem()
                item_icon.setData(1, pixmap)
                self.setItem(row_position, _title_line.index('类型'), item_icon)
                # 插入路径
                item_path = QTableWidgetItem(path)
                self.setItem(row_position, _title_line.index('路径'), item_path)
                # 插入文件名
                filename = function_file_item.get_filename(path)
                item_filename = QTableWidgetItem(filename)
                self.setItem(row_position, _title_line.index('文件名'), item_filename)
                self.item(row_position, _title_line.index('文件名')).setToolTip(filename)
                # 插入预览（空）
                item_preview = QTableWidgetItem()
                self.setItem(row_position, _title_line.index('预览'), item_preview)
                # 插入进度（空）
                item_preview = QTableWidgetItem()
                self.setItem(row_position, _title_line.index('进度'), item_preview)
                # 禁止编辑单元格
                for column in range(self.columnCount()):
                    item = self.item(row_position, column)
                    item.setFlags(item.flags() & ~Qt.ItemIsEditable)  # 禁用单元格编辑

        self.calc_new_filename()
        self._current_order = None

    def calc_new_filename(self):
        """计算新的文件名，并显示在预览列"""
        function_normal.print_function_info()
        rule_class = RenameRule()
        for row in range(self.rowCount()):
            # 先检查单元格是否有附加数据，如果有附加数据，则在附加数据的基础上进行处理，否则按原始路径进行处理
            path = self.item(row, _title_line.index('路径')).text()
            maybe_info_class: RenameInfo = self.item(row, _title_line.index('预览')).data(_data_role)
            if maybe_info_class:
                rename_info_class: RenameInfo = rule_class.calc_new_name(maybe_info_class,
                                                                         row)  # 调用类的方法计算预期文件名，在原信息类的基础上进行处理
            else:
                rename_info_class: RenameInfo = rule_class.calc_new_name(path, row)  # 调用类的方法计算预期文件名，并生成新的重命名信息类
            self.set_cell_data(row, rename_info_class)
            # 更新预览单元格的文本
            calc_filename = rename_info_class.calc_filename
            need_filename = rename_info_class.filename_need
            if calc_filename == need_filename:
                self.item(row, _title_line.index('预览')).setText('')
                self.item(row, _title_line.index('预览')).setToolTip('')
            else:
                self.item(row, _title_line.index('预览')).setText(calc_filename)
                self.item(row, _title_line.index('预览')).setToolTip(calc_filename)
            # 更新原文件名单元格的文本（改名后需要更新为新路径的文件名）
            if self.item(row, _title_line.index('文件名')).text() != need_filename:
                self.item(row, _title_line.index('文件名')).setText(need_filename)

    def rename(self, is_auto_dup):
        """执行重命名"""
        function_normal.print_function_info()
        for row in range(self.rowCount()):
            rename_info_class: RenameInfo = self.item(row, _title_line.index('预览')).data(_data_role)
            # 判断原路径是否存在
            if not os.path.exists(rename_info_class.path_need):
                rename_info_class.set_result_not_exist()
            else:
                rename_info_class = function_normal.calc_final_path(rename_info_class)  # 更新无重复文件名
                if rename_info_class.is_dup:  # 存在重复文件名时进行提示
                    if is_auto_dup:  # 自动处理重命名冲突
                        rename_info_class = self.rename_and_update_class(rename_info_class)  # 更新重命名结果
                    else:
                        reply = self.show_dup_confirm_dialog(rename_info_class.filename_renamed)
                        if reply:
                            rename_info_class = self.rename_and_update_class(rename_info_class)  # 更新重命名结果
                        else:
                            rename_info_class.set_result_skipped()
                else:
                    rename_info_class = self.rename_and_update_class(rename_info_class)  # 更新重命名结果

            # 更新
            self.set_cell_data(row, rename_info_class)
            self.set_result_icon(row, rename_info_class.rename_result)

    def show_dup_confirm_dialog(self, new_filename):
        """在重命名时，遇到重复文件名情况下弹出确认对话框"""
        function_normal.print_function_info()
        reply = QMessageBox.question(self, '重复文件名确认',
                                     f'目录中已存在相同文件名，是否重命名为：\n{new_filename}',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            return True
        else:
            return False

    @staticmethod
    def rename_and_update_class(rename_info_class: RenameInfo):
        """执行重命名"""
        function_normal.print_function_info()
        old_path = rename_info_class.path_need
        final_path = rename_info_class.path_renamed
        final_filetitle = rename_info_class.filetitle_renamed
        # 判断路径是否变化，是否需要执行重命名
        if old_path == final_path:
            rename_info_class.set_result_skipped()
        # 判断文件名是否符合命名规则（只有空格或.等情况）
        elif final_filetitle.count(' ') + final_filetitle.count('.') == len(final_filetitle):
            rename_info_class.set_result_unknown_error()
        # 否则正常执行重命名操作
        else:
            try:
                os.rename(old_path, final_path)
                rename_info_class.set_result_renamed()
            except FileNotFoundError:
                rename_info_class.set_result_not_exist()
            except PermissionError:
                rename_info_class.set_result_occupied()
            except Exception as e:
                print(e)
                rename_info_class.set_result_unknown_error()

        return rename_info_class

    @staticmethod
    def cancel_rename_and_update_class(rename_info_class: RenameInfo):
        """执行重命名"""
        function_normal.print_function_info()
        old_path = rename_info_class.path_need
        final_path = rename_info_class.path_cancel
        try:
            os.rename(old_path, final_path)
            rename_info_class.set_result_cancelled()
        except Exception as e:
            print(e)
            pass

        return rename_info_class

    def cancel_rename(self):
        """撤销重命名"""
        function_normal.print_function_info()
        for row in range(self.rowCount()):
            rename_info_class: RenameInfo = self.item(row, _title_line.index('预览')).data(_data_role)
            # 没有重命名信息类则直接跳过
            if not rename_info_class:
                continue
            # 判断原路径是否存在
            if not os.path.exists(rename_info_class.path_need):
                rename_info_class.set_result_not_exist()
            else:
                cancel_info_class = function_normal.calc_cancelled_path(rename_info_class)  # 计算无重复的文件信息
                # 只在成功修改回原始文件名后才更新重命名结果参数
                if cancel_info_class.is_dup_cancel:  # 存在重复文件名时进行提示
                    reply = self.show_dup_confirm_dialog(cancel_info_class.filename_cancel)
                    if reply:
                        rename_info_class = self.cancel_rename_and_update_class(rename_info_class)
                else:
                    rename_info_class = self.cancel_rename_and_update_class(rename_info_class)
            # 更新
            self.set_cell_data(row, rename_info_class)
            self.set_result_icon(row, rename_info_class.rename_result)

    def set_result_icon(self, row: int, result: str):
        """设置重命名结果的图标"""
        function_normal.print_function_info()
        icon_base64, tip = function_normal.get_icon_result(result)
        pixmap = QPixmap()
        pixmap.loadFromData(icon_base64)
        item_icon = QTableWidgetItem()
        item_icon.setData(1, pixmap)
        item_icon.setToolTip(tip)
        self.setItem(row, _title_line.index('进度'), item_icon)

    def set_cell_data(self, row: int, rename_info_class):
        """设置单元格附加数据"""
        self.item(row, _title_line.index('文件名')).setData(_data_role, rename_info_class)
        self.item(row, _title_line.index('预览')).setData(_data_role, rename_info_class)

    def paths_showed(self):
        """当前显示的路径列表"""
        function_normal.print_function_info()
        paths = []
        for row in range(self.rowCount()):
            # 先尝试提取单元格中的重命名信息类，如果不存在则提取路径列的文本
            info_class:RenameInfo = self.item(row, _title_line.index('文件名')).data(_data_role)
            if info_class:
                path = info_class.path_need
            else:
                path = self.item(row, _title_line.index('路径')).text()
            paths.append(path)
        return paths

    def move_item_up(self):
        """将当前项目向上移动一位"""
        function_normal.print_function_info()
        selected_rows = sorted(set(item.row() for item in self.selectedItems()))

        if selected_rows[0] == 0:  # 选中行中有首行时，不移动
            return

        self.selectionModel().clear()  # 清空选中行
        for row in selected_rows:
            if row > 0:  # 确保上面有一行可以交换
                for column in range(self.columnCount()):
                    item_above = self.takeItem(row - 1, column)
                    item_current = self.takeItem(row, column)
                    self.setItem(row - 1, column, item_current)
                    self.setItem(row, column, item_above)

                    # 重新选中对应行
                    self.selectionModel().select(self.model().index(row - 1, column), QItemSelectionModel.Select)

        self.calc_new_filename()
        self._current_order = None

    def move_item_down(self):
        """将当前项目向下移动一位"""
        function_normal.print_function_info()
        selected_rows = sorted(set(item.row() for item in self.selectedItems()), reverse=True)

        if selected_rows[0] == self.rowCount() - 1:  # 选中行中有尾行时，不移动
            return

        self.selectionModel().clear()  # 清空选中行
        for row in selected_rows:
            if row < self.rowCount() - 1:  # 确保下面有一行可以交换
                for column in range(self.columnCount()):
                    item_below = self.takeItem(row + 1, column)
                    item_current = self.takeItem(row, column)
                    self.setItem(row + 1, column, item_current)
                    self.setItem(row, column, item_below)

                    # 重新选中对应行
                    self.selectionModel().select(self.model().index(row + 1, column), QItemSelectionModel.Select)

        self.calc_new_filename()
        self._current_order = None

    def change_item_position(self, row_1, row_2):
        """互换两个行项目的位置"""
        function_normal.print_function_info()
        for column in range(self.columnCount()):
            item_1 = self.takeItem(row_1, column)
            item_2 = self.takeItem(row_2, column)
            self.setItem(row_1, column, item_2)
            self.setItem(row_2, column, item_1)

    def move_item_top(self):
        """将当前项目移动到顶部"""
        function_normal.print_function_info()
        selected_rows = sorted(set(item.row() for item in self.selectedItems()))

        self.selectionModel().clear()  # 清空选中行
        for index, row in enumerate(selected_rows):
            self.insertRow(index)  # 插入新行
            self.setRowHeight(index, _max_height)  # 锁定新行的行高
            for column in range(self.columnCount()):
                item_take = self.takeItem(row + 1, column)  # 插入一行后行号需要下移一位+1
                self.setItem(index, column, item_take)
            self.removeRow(row + 1)  # 插入一行后行号需要下移一位+1

        # 重新选中对应行，直接从首行开始按顺序选中即可
        for row, _ in enumerate(selected_rows):
            for column in range(self.columnCount()):
                self.selectionModel().select(self.model().index(row, column), QItemSelectionModel.Select)

        self.calc_new_filename()
        self._current_order = None

    def move_item_bottom(self):
        """将当前项目移动到底部"""
        function_normal.print_function_info()
        selected_rows = sorted(set(item.row() for item in self.selectedItems()), reverse=True)

        self.selectionModel().clear()  # 清空选中行
        for index, row in enumerate(selected_rows):
            index = self.rowCount() - index
            self.insertRow(index)  # 插入新行
            self.setRowHeight(index, _max_height)  # 锁定新行的行高
            for column in range(self.columnCount()):
                item_take = self.takeItem(row, column)  # 在下方插入，无需调整行号
                self.setItem(index, column, item_take)
            self.removeRow(row)

        # 重新选中对应行，直接从尾行开始按顺序选中即可
        for row, _ in enumerate(selected_rows):
            row = self.rowCount() - row - 1
            for column in range(self.columnCount()):
                self.selectionModel().select(self.model().index(row, column), QItemSelectionModel.Select)

        self.calc_new_filename()
        self._current_order = None

    def remove_item(self):
        """移除当前项目"""
        function_normal.print_function_info()
        remove_paths = []
        for item in self.selectedItems():
            try:
                row = item.row()
                path = self.item(row, _title_line.index('路径')).text()
                remove_paths.append(path)
                self.removeRow(row)
            except RuntimeError:
                # 由于默认选中整行，selectedItems()会返回该行的所有单元格，从而导致在删除该行的其他单元格时重复删除整行而报错
                pass

        self.calc_new_filename()
        self._current_order = None

        return remove_paths

    def clear_items(self):
        """清空所有项目"""
        function_normal.print_function_info()
        removed_path_class_dict = dict()
        while self.rowCount():
            path = self.item(0, _title_line.index('路径')).text()
            info_class = self.item(0, _title_line.index('预览')).data(_data_role)
            removed_path_class_dict[path] = info_class
            self.removeRow(0)

        self._current_order = None

        return removed_path_class_dict

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        mime_data = event.mimeData()
        if mime_data.hasUrls():
            paths = []
            for url in mime_data.urls():
                path = url.toLocalFile()
                paths.append(path)
            self.insert_path_item(paths)
            event.acceptProposedAction()
