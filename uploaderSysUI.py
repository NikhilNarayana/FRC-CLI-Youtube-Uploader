# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uploaderSysUI.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_uploader_form(object):
    def setupUi(self, uploader_form):
        uploader_form.setObjectName("uploader_form")
        uploader_form.resize(907, 816)
        self.formLayout = QtWidgets.QFormLayout(uploader_form)
        self.formLayout.setObjectName("formLayout")
        self.title = QtWidgets.QLabel(uploader_form)
        self.title.setObjectName("title")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.title)
        self.match_files_loc_label = QtWidgets.QLabel(uploader_form)
        self.match_files_loc_label.setObjectName("match_files_loc_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.match_files_loc_label)
        self.match_files_loc = QtWidgets.QComboBox(uploader_form)
        self.match_files_loc.setObjectName("match_files_loc")
        self.match_files_loc.addItem("")
        self.match_files_loc.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.match_files_loc)
        self.prod_team_label = QtWidgets.QLabel(uploader_form)
        self.prod_team_label.setObjectName("prod_team_label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.prod_team_label)
        self.prod_team = QtWidgets.QPlainTextEdit(uploader_form)
        self.prod_team.setMaximumSize(QtCore.QSize(16777215, 27))
        self.prod_team.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.prod_team.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.prod_team.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.prod_team.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.prod_team.setObjectName("prod_team")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.prod_team)
        self.twitter_handle_label = QtWidgets.QLabel(uploader_form)
        self.twitter_handle_label.setObjectName("twitter_handle_label")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.twitter_handle_label)
        self.facebook_name_label = QtWidgets.QLabel(uploader_form)
        self.facebook_name_label.setObjectName("facebook_name_label")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.facebook_name_label)
        self.facebook_name = QtWidgets.QPlainTextEdit(uploader_form)
        self.facebook_name.setMaximumSize(QtCore.QSize(16777215, 27))
        self.facebook_name.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.facebook_name.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.facebook_name.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.facebook_name.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.facebook_name.setObjectName("facebook_name")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.facebook_name)
        self.website_link_label = QtWidgets.QLabel(uploader_form)
        self.website_link_label.setObjectName("website_link_label")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.website_link_label)
        self.website_link = QtWidgets.QPlainTextEdit(uploader_form)
        self.website_link.setMaximumSize(QtCore.QSize(16777215, 27))
        self.website_link.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.website_link.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.website_link.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.website_link.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.website_link.setObjectName("website_link")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.website_link)
        self.event_name_label = QtWidgets.QLabel(uploader_form)
        self.event_name_label.setObjectName("event_name_label")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.event_name_label)
        self.event_name = QtWidgets.QPlainTextEdit(uploader_form)
        self.event_name.setMaximumSize(QtCore.QSize(16777215, 27))
        self.event_name.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.event_name.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.event_name.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.event_name.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.event_name.setObjectName("event_name")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.event_name)
        self.event_code_label = QtWidgets.QLabel(uploader_form)
        self.event_code_label.setObjectName("event_code_label")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.event_code_label)
        self.event_code = QtWidgets.QPlainTextEdit(uploader_form)
        self.event_code.setMaximumSize(QtCore.QSize(16777215, 27))
        self.event_code.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.event_code.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.event_code.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.event_code.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.event_code.setObjectName("event_code")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.event_code)
        self.playlist_id_label = QtWidgets.QLabel(uploader_form)
        self.playlist_id_label.setObjectName("playlist_id_label")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.playlist_id_label)
        self.playlist_id = QtWidgets.QPlainTextEdit(uploader_form)
        self.playlist_id.setMaximumSize(QtCore.QSize(16777215, 27))
        self.playlist_id.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.playlist_id.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.playlist_id.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.playlist_id.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.playlist_id.setPlainText("")
        self.playlist_id.setOverwriteMode(False)
        self.playlist_id.setObjectName("playlist_id")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.playlist_id)
        self.tba_event_id_label = QtWidgets.QLabel(uploader_form)
        self.tba_event_id_label.setObjectName("tba_event_id_label")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.tba_event_id_label)
        self.tba_event_id = QtWidgets.QPlainTextEdit(uploader_form)
        self.tba_event_id.setMaximumSize(QtCore.QSize(16777215, 27))
        self.tba_event_id.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tba_event_id.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tba_event_id.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tba_event_id.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.tba_event_id.setObjectName("tba_event_id")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.tba_event_id)
        self.tba_event_secret_label = QtWidgets.QLabel(uploader_form)
        self.tba_event_secret_label.setObjectName("tba_event_secret_label")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.tba_event_secret_label)
        self.tba_event_secret = QtWidgets.QPlainTextEdit(uploader_form)
        self.tba_event_secret.setMaximumSize(QtCore.QSize(16777215, 27))
        self.tba_event_secret.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tba_event_secret.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tba_event_secret.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tba_event_secret.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.tba_event_secret.setObjectName("tba_event_secret")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.tba_event_secret)
        self.video_descr_label = QtWidgets.QLabel(uploader_form)
        self.video_descr_label.setObjectName("video_descr_label")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.video_descr_label)
        self.video_descr = QtWidgets.QPlainTextEdit(uploader_form)
        self.video_descr.setMaximumSize(QtCore.QSize(16777215, 54))
        self.video_descr.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.video_descr.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.video_descr.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.video_descr.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.video_descr.setObjectName("video_descr")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.video_descr)
        self.match_code_label = QtWidgets.QLabel(uploader_form)
        self.match_code_label.setObjectName("match_code_label")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.LabelRole, self.match_code_label)
        self.match_code = QtWidgets.QPlainTextEdit(uploader_form)
        self.match_code.setMaximumSize(QtCore.QSize(16777215, 27))
        self.match_code.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.match_code.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.match_code.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.match_code.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.match_code.setObjectName("match_code")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.match_code)
        self.match_number_label = QtWidgets.QLabel(uploader_form)
        self.match_number_label.setObjectName("match_number_label")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.LabelRole, self.match_number_label)
        self.match_num = QtWidgets.QPlainTextEdit(uploader_form)
        self.match_num.setMaximumSize(QtCore.QSize(16777215, 27))
        self.match_num.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.match_num.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.match_num.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.match_num.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.match_num.setObjectName("match_num")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.FieldRole, self.match_num)
        self.match_type_label = QtWidgets.QLabel(uploader_form)
        self.match_type_label.setObjectName("match_type_label")
        self.formLayout.setWidget(15, QtWidgets.QFormLayout.LabelRole, self.match_type_label)
        self.match_type = QtWidgets.QComboBox(uploader_form)
        self.match_type.setObjectName("match_type")
        self.match_type.addItem("")
        self.match_type.addItem("")
        self.match_type.addItem("")
        self.match_type.addItem("")
        self.formLayout.setWidget(15, QtWidgets.QFormLayout.FieldRole, self.match_type)
        self.tiebreaker_label = QtWidgets.QLabel(uploader_form)
        self.tiebreaker_label.setObjectName("tiebreaker_label")
        self.formLayout.setWidget(16, QtWidgets.QFormLayout.LabelRole, self.tiebreaker_label)
        self.tiebreaker = QtWidgets.QComboBox(uploader_form)
        self.tiebreaker.setObjectName("tiebreaker")
        self.tiebreaker.addItem("")
        self.tiebreaker.addItem("")
        self.formLayout.setWidget(16, QtWidgets.QFormLayout.FieldRole, self.tiebreaker)
        self.update_tba_label = QtWidgets.QLabel(uploader_form)
        self.update_tba_label.setObjectName("update_tba_label")
        self.formLayout.setWidget(17, QtWidgets.QFormLayout.LabelRole, self.update_tba_label)
        self.update_tba = QtWidgets.QComboBox(uploader_form)
        self.update_tba.setObjectName("update_tba")
        self.update_tba.addItem("")
        self.update_tba.addItem("")
        self.formLayout.setWidget(17, QtWidgets.QFormLayout.FieldRole, self.update_tba)
        self.ceremonies_label = QtWidgets.QLabel(uploader_form)
        self.ceremonies_label.setObjectName("ceremonies_label")
        self.formLayout.setWidget(18, QtWidgets.QFormLayout.LabelRole, self.ceremonies_label)
        self.ceremonies = QtWidgets.QComboBox(uploader_form)
        self.ceremonies.setObjectName("ceremonies")
        self.ceremonies.addItem("")
        self.ceremonies.addItem("")
        self.ceremonies.addItem("")
        self.ceremonies.addItem("")
        self.formLayout.setWidget(18, QtWidgets.QFormLayout.FieldRole, self.ceremonies)
        self.event_day_label = QtWidgets.QLabel(uploader_form)
        self.event_day_label.setObjectName("event_day_label")
        self.formLayout.setWidget(19, QtWidgets.QFormLayout.LabelRole, self.event_day_label)
        self.event_day = QtWidgets.QComboBox(uploader_form)
        self.event_day.setObjectName("event_day")
        self.event_day.addItem("")
        self.event_day.addItem("")
        self.event_day.addItem("")
        self.event_day.addItem("")
        self.formLayout.setWidget(19, QtWidgets.QFormLayout.FieldRole, self.event_day)
        self.last_match_num_label = QtWidgets.QLabel(uploader_form)
        self.last_match_num_label.setObjectName("last_match_num_label")
        self.formLayout.setWidget(21, QtWidgets.QFormLayout.LabelRole, self.last_match_num_label)
        self.last_match_num = QtWidgets.QPlainTextEdit(uploader_form)
        self.last_match_num.setMaximumSize(QtCore.QSize(16777215, 27))
        self.last_match_num.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.last_match_num.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.last_match_num.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.last_match_num.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.last_match_num.setObjectName("last_match_num")
        self.formLayout.setWidget(21, QtWidgets.QFormLayout.FieldRole, self.last_match_num)
        self.submit = QtWidgets.QPushButton(uploader_form)
        self.submit.setObjectName("submit")
        self.formLayout.setWidget(22, QtWidgets.QFormLayout.LabelRole, self.submit)
        self.twitter_handle = QtWidgets.QPlainTextEdit(uploader_form)
        self.twitter_handle.setMaximumSize(QtCore.QSize(16777215, 26))
        self.twitter_handle.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.twitter_handle.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.twitter_handle.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.twitter_handle.setObjectName("twitter_handle")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.twitter_handle)

        self.retranslateUi(uploader_form)
        QtCore.QMetaObject.connectSlotsByName(uploader_form)

    def retranslateUi(self, uploader_form):
        _translate = QtCore.QCoreApplication.translate
        uploader_form.setWindowTitle(_translate("uploader_form", "Dialog"))
        self.title.setText(_translate("uploader_form", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">FRC Youtube Uploader</span></p></body></html>"))
        self.match_files_loc_label.setText(_translate("uploader_form", "<html><head/><body><p><span style=\" font-size:10pt;\">Match Files Location</span></p></body></html>"))
        self.match_files_loc.setItemText(0, _translate("uploader_form", "Parent Folder to Scripts"))
        self.match_files_loc.setItemText(1, _translate("uploader_form", "Same Folder as Scripts"))
        self.prod_team_label.setText(_translate("uploader_form", "<html><head/><body><p><span style=\" font-size:10pt;\">Production Team</span></p></body></html>"))
        self.twitter_handle_label.setText(_translate("uploader_form", "<html><head/><body><p><span style=\" font-size:10pt;\">Twitter Handle</span></p></body></html>"))
        self.facebook_name_label.setText(_translate("uploader_form", "<html><head/><body><p><span style=\" font-size:10pt;\">Facebook Name</span></p></body></html>"))
        self.website_link_label.setText(_translate("uploader_form", "<html><head/><body><p><span style=\" font-size:10pt;\">Website Link</span></p></body></html>"))
        self.event_name_label.setText(_translate("uploader_form", "<html><head/><body><p><span style=\" font-size:10pt;\">Event Name</span></p></body></html>"))
        self.event_code_label.setText(_translate("uploader_form", "<html><head/><body><p><span style=\" font-size:10pt;\">Event code (ex. 2016arc)</span></p></body></html>"))
        self.playlist_id_label.setText(_translate("uploader_form", "<html><head/><body><p><span style=\" font-size:10pt;\">Playlist ID</span></p></body></html>"))
        self.tba_event_id_label.setText(_translate("uploader_form", "<html><head/><body><p><span style=\" font-size:10pt;\">TBA Event ID</span></p></body></html>"))
        self.tba_event_id.setPlainText(_translate("uploader_form", "Go to thebluealliance.com/request/apiwrite to get keys"))
        self.tba_event_secret_label.setText(_translate("uploader_form", "<html><head/><body><p><span style=\" font-size:10pt;\">TBA Event Secret</span></p></body></html>"))
        self.tba_event_secret.setPlainText(_translate("uploader_form", "Go to thebluealliance.com/request/apiwrite to get keys"))
        self.video_descr_label.setText(_translate("uploader_form", "<html><head/><body><p><span style=\" font-size:10pt;\">Video Description</span></p></body></html>"))
        self.video_descr.setPlainText(_translate("uploader_form", "Add alternate description here."))
        self.match_code_label.setText(_translate("uploader_form", "<html><head/><body><p><span style=\" font-size:10pt;\">Match Code</span></p></body></html>"))
        self.match_number_label.setText(_translate("uploader_form", "<html><head/><body><p><span style=\" font-size:10pt;\">Match Number</span></p></body></html>"))
        self.match_type_label.setText(_translate("uploader_form", "<html><head/><body><p><span style=\" font-size:10pt;\">Match Type</span></p></body></html>"))
        self.match_type.setItemText(0, _translate("uploader_form", "Qualifications"))
        self.match_type.setItemText(1, _translate("uploader_form", "Quarterfinals"))
        self.match_type.setItemText(2, _translate("uploader_form", "Semifinals"))
        self.match_type.setItemText(3, _translate("uploader_form", "Finals"))
        self.tiebreaker_label.setText(_translate("uploader_form", "<html><head/><body><p><span style=\" font-size:10pt;\">Tiebreaker</span></p></body></html>"))
        self.tiebreaker.setItemText(0, _translate("uploader_form", "No"))
        self.tiebreaker.setItemText(1, _translate("uploader_form", "Yes"))
        self.update_tba_label.setText(_translate("uploader_form", "<html><head/><body><p><span style=\" font-size:10pt;\">Update TBA</span></p></body></html>"))
        self.update_tba.setItemText(0, _translate("uploader_form", "Yes"))
        self.update_tba.setItemText(1, _translate("uploader_form", "No"))
        self.ceremonies_label.setText(_translate("uploader_form", "<html><head/><body><p><span style=\" font-size:10pt;\">Ceremonies</span></p></body></html>"))
        self.ceremonies.setItemText(0, _translate("uploader_form", "None"))
        self.ceremonies.setItemText(1, _translate("uploader_form", "Opening Ceremonies"))
        self.ceremonies.setItemText(2, _translate("uploader_form", "Alliance Selection"))
        self.ceremonies.setItemText(3, _translate("uploader_form", "Closing Ceremonies"))
        self.event_day_label.setText(_translate("uploader_form", "<html><head/><body><p><span style=\" font-size:10pt;\">Event Day</span></p></body></html>"))
        self.event_day.setItemText(0, _translate("uploader_form", "Ignore"))
        self.event_day.setItemText(1, _translate("uploader_form", "1"))
        self.event_day.setItemText(2, _translate("uploader_form", "2"))
        self.event_day.setItemText(3, _translate("uploader_form", "3"))
        self.last_match_num_label.setText(_translate("uploader_form", "<html><head/><body><p><span style=\" font-size:10pt;\">Last Match Number</span></p></body></html>"))
        self.last_match_num.setPlainText(_translate("uploader_form", "Only for batch uploads"))
        self.submit.setText(_translate("uploader_form", "Submit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    uploader_form = QtWidgets.QDialog()
    ui = Ui_uploader_form()
    ui.setupUi(uploader_form)
    uploader_form.show()
    sys.exit(app.exec_())
