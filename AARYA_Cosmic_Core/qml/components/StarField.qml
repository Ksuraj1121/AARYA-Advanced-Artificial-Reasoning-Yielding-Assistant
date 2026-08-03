import QtQuick

Item {
    anchors.fill: parent

    Repeater {
        model: 150

        Rectangle {
            width: Math.random() * 3 + 1
            height: width
            radius: width

            color: "#AEEBFF"

            x: Math.random() * parent.width
            y: Math.random() * parent.height

            opacity: Math.random()

            SequentialAnimation on opacity {
                loops: Animation.Infinite

                NumberAnimation {
                    to: 1.0
                    duration: 1000 + Math.random() * 3000
                }

                NumberAnimation {
                    to: 0.15
                    duration: 1000 + Math.random() * 3000
                }
            }
        }
    }
}