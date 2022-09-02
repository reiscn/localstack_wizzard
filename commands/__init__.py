import subprocess

from constants import LOCALSTACK_HOST, LOCALSTACK_QUEUE_PREFIX

def runBashCmd(bash_cmd):
    result = subprocess.run(bash_cmd, shell=True, capture_output=True)
    result_stdout = result.stdout.decode("utf-8")
    result_error = has_error(result.stderr.decode("utf-8"))
    is_result_empty = is_emtpy(result_stdout)

    if result_error:
        raise Exception(f"Failed to invoke bash command:\n\n{bash_cmd}\n\nCheck if queue and" +
        "payload file names are correct!\n\n")

    if is_result_empty:
        return None
    else: 
        return result_stdout

def has_error(bash_std_err):
    return str(bash_std_err) != ""

def is_emtpy(bash_std_out):
    return str(bash_std_out) == ""

def get_queue_full_url(queue_name):
    return LOCALSTACK_HOST + LOCALSTACK_QUEUE_PREFIX + queue_name

def send_message(queue_name, payload_file_name):
    print(f"** Sending send-message command to {queue_name}")
    print(f"** Trying to obtain payload from file, provided file is {payload_file_name}")
    print(f"** Sending message to SQS queue: {queue_name}")

    bash_cmd = "aws --endpoint-url " + LOCALSTACK_HOST + " sqs send-message --queue-url " + get_queue_full_url(queue_name) + " --message-body file://" + payload_file_name
    print(f"** Invoking bash cmd: {bash_cmd}")
    
    try:
        runBashCmd(bash_cmd)
        print("** Done")
    except Exception as e:
        print(f"** A problem occured: {e}")

def purge(queue_name):
    print(f"** Sending purge command to {queue_name}")
    bash_cmd = "aws --endpoint-url " + LOCALSTACK_HOST + " sqs purge-queue --queue-url " + get_queue_full_url(queue_name)
    print(f"** Invoking bash cmd: {bash_cmd}")

    try:
        runBashCmd(bash_cmd)
        print("** Queue successfully purged")
    except Exception as e:
        print(f"A problem occured: {e}")

def receive_messages(queue_name, amount=1):
    print(f"** Sending receive-message command to {queue_name}")
    print(f"** Trying to obtain {amount} messages from queue")
    bash_cmd = "aws --endpoint-url " + LOCALSTACK_HOST + " sqs receive-message --queue-url " + get_queue_full_url(queue_name) + " --max-number-of-messages " + str(amount)
    
    try:
        result = runBashCmd(bash_cmd)
    except Exception as e:
        print(f"A problem occured: {e}")

    if not result:
        print("** No messages in queue")
    else:
        print(f"** Message: \n\n {result}")

def clear_console():
    runBashCmd("clear")