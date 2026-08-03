import QtQuick

Rectangle {

    width: 260
    height: 260
    radius: width / 2

    color: "#00D9FF"
    opacity: 0.10

    SequentialAnimation on scale {

        loops: Animation.Infinite

        NumberAnimation {
            from: 1.0
            to: 1.25
            duration: 1500
        }

        NumberAnimation {
            from: 1.25
            to: 1.0
            duration: 1500
        }
    }
}