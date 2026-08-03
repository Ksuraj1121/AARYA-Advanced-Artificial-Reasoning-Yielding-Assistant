import QtQuick

Item {
    width: 140
    height: 40

    property string currentTime: ""

    Timer {
        interval: 1000
        running: true
        repeat: true

        onTriggered: {
            currentTime = Qt.formatTime(new Date(), "hh:mm:ss")
        }
    }

    Component.onCompleted: {
        currentTime = Qt.formatTime(new Date(), "hh:mm:ss")
    }

    Text {
        anchors.centerIn: parent
        text: currentTime
        color: "#00D9FF"
        font.pixelSize: 22
        font.bold: true
    }
}