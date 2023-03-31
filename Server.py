from pydbus import SessionBus  # Session or System Bus
from gi.repository import GLib

bus = SessionBus()
BUS = "org.example.demo.test"
loop = GLib.MainLoop()
INTERVAL = 2
message_count = 0

class DBusService_XML:  # method name="server_no_args"
    """
    DBus Service XML definition
    type = "i" for integer, "S" string, "d" double, "as" list of string data
    """
    dbus = """
    <node>
        <interface name= "{}">
            <method name="server_no_args">
            </method>
        <interface>
    </node>
    """.format(BUS)

    def server_no_args(self):
        "No arguments over the dbus. Server produces a message on the console."
        global message_count
        print("This is message {}".format(message_count))
        message_count += 1


if __name__ == "__main__":
    bus.publish(BUS, DBusService_XML())
    loop.run()