from PySide2 import QtWidgets


class TPProfile(QtWidgets.QWidget):
    def __init__(self, settings):
        super(TPProfile, self).__init__()

        # Layout
        self.mainlayout = QtWidgets.QVBoxLayout()
        self.mainlayout.setContentsMargins(5, 5, 5, 5)

        # Widgets
        introductionText = QtWidgets.QLabel()
        introductionText.setText(settings["introText"])
        introductionText.setWordWrap(True)

        # ---- Property List Section ----
        propertyList = QtWidgets.QTextEdit()
        propertyList.setReadOnly(True)
        propertyList.setText(
            "<html><ul>"
            + "".join([f"<li>{name}</li>" for name in settings["propertyLabels"]])
            + "</ul></html>"
        )

        # ---- Display TPP Section ----
        self.displayTPP = QtWidgets.QTextEdit()
        self.displayTPP.setReadOnly(True)
        self.displayTPP.setText(
            "<html><ul>"
            + "".join([f"<li>{name}</li>" for name in settings["propertyLabels"]])
            + "</ul></html>"
        )

        self.mainlayout.addWidget(introductionText)
        self.mainlayout.addWidget(propertyList)
        self.mainlayout.addWidget(QHLine())
        self.mainlayout.addWidget(self.displayTPP)
        self.setLayout(self.mainlayout)

    def updateMolProperties(self, propertyDict):
        "update displayed properties when molecule is changed"
        stringToDisplay = ["<html><table>"]
        for prop in propertyDict:
            value = propertyDict[prop]
            if isinstance(value, (int, float, complex)):
                if "yield" in prop.lower():
                    stringToDisplay.append(f"<tr><td><b>{prop}</b>:</td> <td align='right'>{value:.2f}%</td> </tr>")
                elif "deviation" in prop.lower():
                    stringToDisplay.append(f"<tr><td><b>{prop}</b>:</td> <td align='right'>{value:.2f}</td> </tr>")
                else:    
                    stringToDisplay.append(f"<tr><td><b>{prop}</b>:</td> <td align='right'>{(value * 100):.2f}%</td> </tr>")
            elif isinstance(value, str):
                stringToDisplay.append(f"<tr><td><b>{prop}</b>:</td> <td align='left'>{value}</td> </tr>")
            else:
                stringToDisplay.append(f"<tr><td><b>{prop}</b>:</td> <td align='left'>{str(value)}</td> </tr>")
        stringToDisplay.append("</table></html>")
        self.displayTPP.setText("".join(stringToDisplay))


class QHLine(QtWidgets.QFrame):
    def __init__(self):
        super(QHLine, self).__init__()
        self.setFrameShape(QtWidgets.QFrame.HLine)
        self.setFrameShadow(QtWidgets.QFrame.Sunken)


class QVLine(QtWidgets.QFrame):
    def __init__(self):
        super(QVLine, self).__init__()
        self.setFrameShape(QtWidgets.QFrame.VLine)
        self.setFrameShadow(QtWidgets.QFrame.Sunken)
