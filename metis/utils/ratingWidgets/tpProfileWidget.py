from PySide2 import QtWidgets


class TPProfile(QtWidgets.QWidget):
    def __init__(self, settings):
        super(TPProfile, self).__init__()

        # Layout
        self.mainlayout = QtWidgets.QVBoxLayout()

        # Widgets
        introductionText = QtWidgets.QLabel()
        introductionText.setText(settings["introText"])
        introductionText.setWordWrap(True)

        propertyList = QtWidgets.QLabel()
        propertyList.setText(
            "<html><ul>"
            + "".join([f"<li>{name}</li>" for name in settings["propertyLabels"]])
            + "</ul></html>"
        )

        self.displayTPP = QtWidgets.QLabel()
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
        for i in propertyDict:
            value = propertyDict[i]
            if isinstance(value, (int, float, complex)):
                stringToDisplay.append(f"<tr><td>{i}:</td> <td align='right'>{(value*100):.2f}%</td> </tr>")
            elif isinstance(value, str):
                stringToDisplay.append(f"<tr><td>{i}:</td> <td align='right'>{value}</td> </tr>")
            else:
                stringToDisplay.append(f"<tr><td>{i}:</td> <td align='right'>{str(value)}</td> </tr>")
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
