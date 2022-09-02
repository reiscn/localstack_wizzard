from constants import LOCALSTACK_HOST, LOCALSTACK_QUEUE_PREFIX

def print_banner():
    print(
        f"""
        *********************************************************************************************************
        *                                                                                                       *
        *    ooooo                                      oooo               .                       oooo         *
        *   `888'                                      `888             .o8                       `888          *
        *    888          .ooooo.   .ooooo.   .oooo.    888   .oooo.o .o888oo  .oooo.    .ooooo.   888  oooo    *
        *    888         d88' `88b d88' `"Y8 `P  )88b   888  d88(  "8   888   `P  )88b  d88' `"Y8  888 .8P'     *
        *    888         888   888 888        .oP"888   888  `"Y88b.    888    .oP"888  888        888888.      *
        *    888       o 888   888 888   .o8 d8(  888   888  o.  )88b   888 . d8(  888  888   .o8  888 `88b.    *
        *    o888ooooood8 `Y8bod8P' `Y8bod8P' `Y888""8o o888o 8""888P'   "888" `Y888""8o `Y8bod8P' o888o o888o  *
        *                                                                                                       *
        *                                                                                                       *
        *                                                                                                       *
        *    oooooo   oooooo     oooo  o8o                                                 .o8                  *
        *    `888.    `888.     .8'   `"'                                                "888                   *
        *    `888.   .8888.   .8'   oooo    oooooooo   oooooooo  .oooo.   oooo d8b  .oooo888                    *
        *    `888  .8'`888. .8'    `888   d'""7d8P   d'""7d8P  `P  )88b  `888""8P d88' `888                     *
        *    `888.8'  `888.8'      888     .d8P'      .d8P'    .oP"888   888     888   888                      *
        *    `888'    `888'       888   .d8P'  .P  .d8P'  .P d8(  888   888     888   888                       *
        *    `8'      `8'       o888o d8888888P  d8888888P  `Y888""8o d888b    `Y8bod88P"                       *
        *                                                                                                       *
        *                                                                                                       *
        *   written by reisenc                                                                                  *
        *                                                                                                       *
        *   - Implemented to facilitate working with SQS queues in localstack environment                       * 
        *   - Send messages, receive messages, purge queues                                                     *
        *                                                                                                       *
        *   Important: Please ensure that your payload files are located in the same directory as the script!   *
        *                                                                                                       *
        *                                                                                                       *
        *   Current setup: Host={LOCALSTACK_HOST}, Queue prefix={LOCALSTACK_QUEUE_PREFIX}                       *
        *                                                                                                       *
        *********************************************************************************************************                                                                                         
        """
    )

def print_help():
    print(
        """
        +++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        +                                                       +   
        +   Commands:                                           +   
        +   1 - Push message into queue                         +
        +   2 - Purge queue                                     +  
        +   3 - Receive messages (default: 1 message)           +  
        +                                                       +
        +   Type [help] to show help                            +
        +   Type [clear] to clear console                       +
        +   Type [end] to exit script                           +
        +   Type [reset] to reset script (choose new queue)     +
        +                                                       +
        +++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        """
    )