import QtQuick

Text {

    text: "WELCOME BOSS"

    color: "#00D9FF"

    font.pixelSize: 28
    font.bold: true

    opacity: 0

    SequentialAnimation on opacity {

        running: true

        NumberAnimation {
            from: 0
            to: 1
            duration: 2000
        }
    }
}