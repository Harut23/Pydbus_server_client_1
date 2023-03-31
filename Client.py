from pydbus import SessionBus
from gi.repository import GLib
from gi.repository import Gio, GLib, GObject


bus = SessionBus()
BUS = "org.example.demo.test"
server_object = bus.get(BUS)
loop = GLib.MainLoop()
INTERVAL = 2


def make_method_call_client_1():
    print("sending method call: server_no_args")

    # method call to server
    reply = server_object.server_no_args()
    return True


if __name__ == "__main__":
    print("Starting Client Demo ..")
    # call function to make a method call.

    # GLib to run repeating function every 2 secconds
    GLib.timeout_add_seconds(interval=INTERVAL,
                             function=make_method_call_client_1())
    loop.run()