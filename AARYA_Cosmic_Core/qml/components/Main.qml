import QtQuick
import QtQuick.Window
import "components"

Window {
    id: root

    visible: true
    width: 1600
    height: 900

    title: "AARYA Cosmic Core"

    color: "#05070A"

    Rectangle {
        anchors.fill: parent
        color: "#05070A"

        // ----------------------------
        // Animated Star Background
        // ----------------------------

        Repeater {
            model: 200

            Rectangle {
                width: 2
                height: 2
                radius: 1

                color: "white"

                x: Math.random() * parent.width
                y: Math.random() * parent.height

                opacity: 0.2 + Math.random() * 0.8

                SequentialAnimation on opacity {
                    loops: Animation.Infinite

                    NumberAnimation {
                        to: 1.0
                        duration: 1200 + Math.random() * 1500
                    }

                    NumberAnimation {
                        to: 0.2
                        duration: 1200 + Math.random() * 1500
                    }
                }
            }
        }

        // ----------------------------
        // AI Core
        // ----------------------------

        AICore {
            anchors.centerIn: parent
        }
    }
}