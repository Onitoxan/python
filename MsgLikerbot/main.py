# import time
import time

import data_load

FATHER_CHAT_ID = 610513796

def main():
    last_update_id = None
    try:
        while True:
            updates = data_load.get_updates(last_update_id)
            if len(updates.get("result"))> 0:
                last_update_id = data_load.get_last_update_id(updates) + 1
                data_load.echo_all(updates)

            time.sleep(0.5)
    except Exception as e:
        data_load.send_message("Error en el main obteniendo result"+str(e),FATHER_CHAT_ID)


if __name__ == '__main__':
    main()
