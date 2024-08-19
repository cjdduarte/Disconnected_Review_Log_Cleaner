# -*- coding: utf-8 -*-
# Copyright(C)   | Carlos Duarte
# License        | GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html
# Source in      | https://github.com/cjdduarte/Disconnected_Review_Log_Cleaner

from aqt import mw
from aqt.qt import QAction
from aqt.utils import showInfo, askUser

def cleanDisconnectedReviewLogs():
    # Count disconnected review log entries
    count = mw.col.db.scalar("SELECT count(*) FROM revlog WHERE cid NOT IN (SELECT id FROM cards)")

    if count == 0:
        showInfo("No disconnected review log entries found.")
        return

    msg = f"There are {count} disconnected review log entries. If deleted, a full resynchronization will be required afterward. Do you wish to continue?"

    if not askUser(msg):
        return

    mw.col.modSchema(check=True) # New

    mw.progress.start(immediate=True)
    mw.col.db.execute("DELETE FROM revlog WHERE cid NOT IN (SELECT id FROM cards)")
    mw.col.setMod()
    mw.col.save()
    mw.progress.finish()
    mw.requireReset()  # New

    showInfo(f"Removed {count} disconnected review log entries successfully.")

# Add to Tools menu
menu_label = 'Clean Disconnected Review Logs'
action = QAction(menu_label, mw)
action.triggered.connect(cleanDisconnectedReviewLogs)
mw.form.menuTools.addAction(action)
