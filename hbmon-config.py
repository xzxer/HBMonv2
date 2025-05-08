##### Version 2.0.1 #####
#####  DOCKER CONFIG ONLY USE THIS WHEN USING A DOCKERIZED ENVIROMENT #####
CONFIG_INC      = True                           # Include HBlink stats
HOMEBREW_INC    = True                           # Display Homebrew Peers status
LASTHEARD_INC   = True                           # Display lastheard table on main page
LASTHEARD_NUM   = 100
BRIDGES_INC     = False                          # Display Bridge status and button
EMPTY_MASTERS   = False                          # Display Enable (True) or DISABLE (False) empty masters in status
#
HBLINK_IP       = '172.16.238.10'                # HBlink's IP Address (Normally 127.0.0.1)
HBLINK_PORT     = 4321                           # HBlink's TCP reporting socket
FREQUENCY       = 10                             # Frequency to push updates to web clients
CLIENT_TIMEOUT  = 0                              # Clients are timed out after this many seconds, 0 to disable

# Generally you don't need to use this but
# if you don't want to show in lastherad received traffic from OBP link put NETWORK ID 
# for example: "260210,260211,260212"
OPB_FILTER = ""

# Files and stuff for loading alias files for mapping numbers to names
PATH            = './data/'                      # MUST END IN '/'
PEER_FILE       = 'peer_ids.json'                # Will auto-download 
SUBSCRIBER_FILE = 'subscriber_ids.json'          # Will auto-download 
TGID_FILE       = 'talkgroup_ids.json'           # User provided
LOCAL_SUB_FILE  = 'local_subscriber_ids.json'    # User provided (optional, leave '' if you don't use it)
LOCAL_PEER_FILE = 'local_peer_ids.json'          # User provided (optional, leave '' if you don't use it)
LOCAL_TGID_FILE = 'local_talkgroup_ids.json'     # User provided (optional, leave '' if you don't use it)
FILE_RELOAD     = 28                             # Number of days before we reload RadioID.net database files
PEER_URL        = 'https://radioid.net/static/rptrs.json'
SUBSCRIBER_URL  = 'https://radioid.net/static/users.json'

# Settings for log files
LOG_PATH        = './log/'                       # MUST END IN '/'
LOG_NAME        = 'hbmon.log'