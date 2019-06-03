# flags, enums, guids used with DeviceIoControl from WinIoCtl.h

import pywintypes
from ntsecuritycon import FILE_READ_DATA, FILE_WRITE_DATA


def CTL_CODE(DeviceType, Function, Method, Access):
    return (DeviceType << 16) | (Access << 14) | (Function << 2) | Method


def DEVICE_TYPE_FROM_CTL_CODE(ctrlCode):
    return (ctrlCode & 0xffff0000) >> 16


FILE_DEVICE_BEEP = 0x00000001
FILE_DEVICE_CD_ROM = 0x00000002
FILE_DEVICE_CD_ROM_FILE_SYSTEM = 0x00000003
FILE_DEVICE_CONTROLLER = 0x00000004
FILE_DEVICE_DATALINK = 0x00000005
FILE_DEVICE_DFS = 0x00000006
FILE_DEVICE_DISK = 0x00000007
FILE_DEVICE_DISK_FILE_SYSTEM = 0x00000008
FILE_DEVICE_FILE_SYSTEM = 0x00000009
FILE_DEVICE_INPORT_PORT = 0x0000000a
FILE_DEVICE_KEYBOARD = 0x0000000b
FILE_DEVICE_MAILSLOT = 0x0000000c
FILE_DEVICE_MIDI_IN = 0x0000000d
FILE_DEVICE_MIDI_OUT = 0x0000000e
FILE_DEVICE_MOUSE = 0x0000000f
FILE_DEVICE_MULTI_UNC_PROVIDER = 0x00000010
FILE_DEVICE_NAMED_PIPE = 0x00000011
FILE_DEVICE_NETWORK = 0x00000012
FILE_DEVICE_NETWORK_BROWSER = 0x00000013
FILE_DEVICE_NETWORK_FILE_SYSTEM = 0x00000014
FILE_DEVICE_NULL = 0x00000015
FILE_DEVICE_PARALLEL_PORT = 0x00000016
FILE_DEVICE_PHYSICAL_NETCARD = 0x00000017
FILE_DEVICE_PRINTER = 0x00000018
FILE_DEVICE_SCANNER = 0x00000019
FILE_DEVICE_SERIAL_MOUSE_PORT = 0x0000001a
FILE_DEVICE_SERIAL_PORT = 0x0000001b
FILE_DEVICE_SCREEN = 0x0000001c
FILE_DEVICE_SOUND = 0x0000001d
FILE_DEVICE_STREAMS = 0x0000001e
FILE_DEVICE_TAPE = 0x0000001f
FILE_DEVICE_TAPE_FILE_SYSTEM = 0x00000020
FILE_DEVICE_TRANSPORT = 0x00000021
FILE_DEVICE_UNKNOWN = 0x00000022
FILE_DEVICE_VIDEO = 0x00000023
FILE_DEVICE_VIRTUAL_DISK = 0x00000024
FILE_DEVICE_WAVE_IN = 0x00000025
FILE_DEVICE_WAVE_OUT = 0x00000026
FILE_DEVICE_8042_PORT = 0x00000027
FILE_DEVICE_NETWORK_REDIRECTOR = 0x00000028
FILE_DEVICE_BATTERY = 0x00000029
FILE_DEVICE_BUS_EXTENDER = 0x0000002a
FILE_DEVICE_MODEM = 0x0000002b
FILE_DEVICE_VDM = 0x0000002c
FILE_DEVICE_MASS_STORAGE = 0x0000002d
FILE_DEVICE_SMB = 0x0000002e
FILE_DEVICE_KS = 0x0000002f
FILE_DEVICE_CHANGER = 0x00000030
FILE_DEVICE_SMARTCARD = 0x00000031
FILE_DEVICE_ACPI = 0x00000032
FILE_DEVICE_DVD = 0x00000033
FILE_DEVICE_FULLSCREEN_VIDEO = 0x00000034
FILE_DEVICE_DFS_FILE_SYSTEM = 0x00000035
FILE_DEVICE_DFS_VOLUME = 0x00000036
FILE_DEVICE_SERENUM = 0x00000037
FILE_DEVICE_TERMSRV = 0x00000038
FILE_DEVICE_KSEC = 0x00000039
FILE_DEVICE_FIPS = 0x0000003A
FILE_DEVICE_INFINIBAND = 0x0000003B

METHOD_BUFFERED = 0
METHOD_IN_DIRECT = 1
METHOD_OUT_DIRECT = 2
METHOD_NEITHER = 3
METHOD_DIRECT_TO_HARDWARE = METHOD_IN_DIRECT
METHOD_DIRECT_FROM_HARDWARE = METHOD_OUT_DIRECT
FILE_ANY_ACCESS = 0
FILE_SPECIAL_ACCESS = FILE_ANY_ACCESS
FILE_READ_ACCESS = 0x0001
FILE_WRITE_ACCESS = 0x0002
IOCTL_STORAGE_BASE = FILE_DEVICE_MASS_STORAGE
RECOVERED_WRITES_VALID = 0x00000001
UNRECOVERED_WRITES_VALID = 0x00000002
RECOVERED_READS_VALID = 0x00000004
UNRECOVERED_READS_VALID = 0x00000008
WRITE_COMPRESSION_INFO_VALID = 0x00000010
READ_COMPRESSION_INFO_VALID = 0x00000020
TAPE_RETURN_STATISTICS = 0
TAPE_RETURN_ENV_INFO = 1
TAPE_RESET_STATISTICS = 2
MEDIA_ERASEABLE = 0x00000001
MEDIA_WRITE_ONCE = 0x00000002
MEDIA_READ_ONLY = 0x00000004
MEDIA_READ_WRITE = 0x00000008
MEDIA_WRITE_PROTECTED = 0x00000100
MEDIA_CURRENTLY_MOUNTED = 0x80000000
IOCTL_DISK_BASE = FILE_DEVICE_DISK
PARTITION_ENTRY_UNUSED = 0x00
PARTITION_FAT_12 = 0x01
PARTITION_XENIX_1 = 0x02
PARTITION_XENIX_2 = 0x03
PARTITION_FAT_16 = 0x04
PARTITION_EXTENDED = 0x05
PARTITION_HUGE = 0x06
PARTITION_IFS = 0x07
PARTITION_OS2BOOTMGR = 0x0A
PARTITION_FAT32 = 0x0B
PARTITION_FAT32_XINT13 = 0x0C
PARTITION_XINT13 = 0x0E
PARTITION_XINT13_EXTENDED = 0x0F
PARTITION_PREP = 0x41
PARTITION_LDM = 0x42
PARTITION_UNIX = 0x63
VALID_NTFT = 0xC0
PARTITION_NTFT = 0x80

GPT_ATTRIBUTE_PLATFORM_REQUIRED = 0x0000000000000001
GPT_BASIC_DATA_ATTRIBUTE_NO_DRIVE_LETTER = 0x8000000000000000
GPT_BASIC_DATA_ATTRIBUTE_HIDDEN = 0x4000000000000000
GPT_BASIC_DATA_ATTRIBUTE_SHADOW_COPY = 0x2000000000000000
GPT_BASIC_DATA_ATTRIBUTE_READ_ONLY = 0x1000000000000000

HIST_NO_OF_BUCKETS = 24
DISK_LOGGING_START = 0
DISK_LOGGING_STOP = 1
DISK_LOGGING_DUMP = 2
DISK_BINNING = 3
CAP_ATA_ID_CMD = 1
CAP_ATAPI_ID_CMD = 2
CAP_SMART_CMD = 4
ATAPI_ID_CMD = 0xA1
ID_CMD = 0xEC
SMART_CMD = 0xB0
SMART_CYL_LOW = 0x4F
SMART_CYL_HI = 0xC2
SMART_NO_ERROR = 0
SMART_IDE_ERROR = 1
SMART_INVALID_FLAG = 2
SMART_INVALID_COMMAND = 3
SMART_INVALID_BUFFER = 4
SMART_INVALID_DRIVE = 5
SMART_INVALID_IOCTL = 6
SMART_ERROR_NO_MEM = 7
SMART_INVALID_REGISTER = 8
SMART_NOT_SUPPORTED = 9
SMART_NO_IDE_DEVICE = 10
SMART_OFFLINE_ROUTINE_OFFLINE = 0
SMART_SHORT_SELFTEST_OFFLINE = 1
SMART_EXTENDED_SELFTEST_OFFLINE = 2
SMART_ABORT_OFFLINE_SELFTEST = 127
SMART_SHORT_SELFTEST_CAPTIVE = 129
SMART_EXTENDED_SELFTEST_CAPTIVE = 130
READ_ATTRIBUTE_BUFFER_SIZE = 512
IDENTIFY_BUFFER_SIZE = 512
READ_THRESHOLD_BUFFER_SIZE = 512
SMART_LOG_SECTOR_SIZE = 512
READ_ATTRIBUTES = 0xD0
READ_THRESHOLDS = 0xD1
ENABLE_DISABLE_AUTOSAVE = 0xD2
SAVE_ATTRIBUTE_VALUES = 0xD3
EXECUTE_OFFLINE_DIAGS = 0xD4
SMART_READ_LOG = 0xD5
SMART_WRITE_LOG = 0xd6
ENABLE_SMART = 0xD8
DISABLE_SMART = 0xD9
RETURN_SMART_STATUS = 0xDA
ENABLE_DISABLE_AUTO_OFFLINE = 0xDB
IOCTL_CHANGER_BASE = FILE_DEVICE_CHANGER
MAX_VOLUME_ID_SIZE = 36
MAX_VOLUME_TEMPLATE_SIZE = 40
VENDOR_ID_LENGTH = 8
PRODUCT_ID_LENGTH = 16
REVISION_LENGTH = 4
SERIAL_NUMBER_LENGTH = 32
CHANGER_BAR_CODE_SCANNER_INSTALLED = 0x00000001
CHANGER_INIT_ELEM_STAT_WITH_RANGE = 0x00000002
CHANGER_CLOSE_IEPORT = 0x00000004
CHANGER_OPEN_IEPORT = 0x00000008
CHANGER_STATUS_NON_VOLATILE = 0x00000010
CHANGER_EXCHANGE_MEDIA = 0x00000020
CHANGER_CLEANER_SLOT = 0x00000040
CHANGER_LOCK_UNLOCK = 0x00000080
CHANGER_CARTRIDGE_MAGAZINE = 0x00000100
CHANGER_MEDIUM_FLIP = 0x00000200
CHANGER_POSITION_TO_ELEMENT = 0x00000400
CHANGER_REPORT_IEPORT_STATE = 0x00000800
CHANGER_STORAGE_DRIVE = 0x00001000
CHANGER_STORAGE_IEPORT = 0x00002000
CHANGER_STORAGE_SLOT = 0x00004000
CHANGER_STORAGE_TRANSPORT = 0x00008000
CHANGER_DRIVE_CLEANING_REQUIRED = 0x00010000
CHANGER_PREDISMOUNT_EJECT_REQUIRED = 0x00020000
CHANGER_CLEANER_ACCESS_NOT_VALID = 0x00040000
CHANGER_PREMOUNT_EJECT_REQUIRED = 0x00080000
CHANGER_VOLUME_IDENTIFICATION = 0x00100000
CHANGER_VOLUME_SEARCH = 0x00200000
CHANGER_VOLUME_ASSERT = 0x00400000
CHANGER_VOLUME_REPLACE = 0x00800000
CHANGER_VOLUME_UNDEFINE = 0x01000000
CHANGER_SERIAL_NUMBER_VALID = 0x04000000
CHANGER_DEVICE_REINITIALIZE_CAPABLE = 0x08000000
CHANGER_KEYPAD_ENABLE_DISABLE = 0x10000000
CHANGER_DRIVE_EMPTY_ON_DOOR_ACCESS = 0x20000000

CHANGER_RESERVED_BIT = 0x80000000
CHANGER_PREDISMOUNT_ALIGN_TO_SLOT = 0x80000001
CHANGER_PREDISMOUNT_ALIGN_TO_DRIVE = 0x80000002
CHANGER_CLEANER_AUTODISMOUNT = 0x80000004
CHANGER_TRUE_EXCHANGE_CAPABLE = 0x80000008
CHANGER_SLOTS_USE_TRAYS = 0x80000010
CHANGER_RTN_MEDIA_TO_ORIGINAL_ADDR = 0x80000020
CHANGER_CLEANER_OPS_NOT_SUPPORTED = 0x80000040
CHANGER_IEPORT_USER_CONTROL_OPEN = 0x80000080
CHANGER_IEPORT_USER_CONTROL_CLOSE = 0x80000100
CHANGER_MOVE_EXTENDS_IEPORT = 0x80000200
CHANGER_MOVE_RETRACTS_IEPORT = 0x80000400


CHANGER_TO_TRANSPORT = 0x01
CHANGER_TO_SLOT = 0x02
CHANGER_TO_IEPORT = 0x04
CHANGER_TO_DRIVE = 0x08
LOCK_UNLOCK_IEPORT = 0x01
LOCK_UNLOCK_DOOR = 0x02
LOCK_UNLOCK_KEYPAD = 0x04
LOCK_ELEMENT = 0
UNLOCK_ELEMENT = 1
EXTEND_IEPORT = 2
RETRACT_IEPORT = 3
ELEMENT_STATUS_FULL = 0x00000001
ELEMENT_STATUS_IMPEXP = 0x00000002
ELEMENT_STATUS_EXCEPT = 0x00000004
ELEMENT_STATUS_ACCESS = 0x00000008
ELEMENT_STATUS_EXENAB = 0x00000010
ELEMENT_STATUS_INENAB = 0x00000020
ELEMENT_STATUS_PRODUCT_DATA = 0x00000040
ELEMENT_STATUS_LUN_VALID = 0x00001000
ELEMENT_STATUS_ID_VALID = 0x00002000
ELEMENT_STATUS_NOT_BUS = 0x00008000
ELEMENT_STATUS_INVERT = 0x00400000
ELEMENT_STATUS_SVALID = 0x00800000
ELEMENT_STATUS_PVOLTAG = 0x10000000
ELEMENT_STATUS_AVOLTAG = 0x20000000
ERROR_LABEL_UNREADABLE = 0x00000001
ERROR_LABEL_QUESTIONABLE = 0x00000002
ERROR_SLOT_NOT_PRESENT = 0x00000004
ERROR_DRIVE_NOT_INSTALLED = 0x00000008
ERROR_TRAY_MALFUNCTION = 0x00000010
ERROR_INIT_STATUS_NEEDED = 0x00000011
ERROR_UNHANDLED_ERROR = 0xFFFFFFFF
SEARCH_ALL = 0x0
SEARCH_PRIMARY = 0x1
SEARCH_ALTERNATE = 0x2
SEARCH_ALL_NO_SEQ = 0x4
SEARCH_PRI_NO_SEQ = 0x5
SEARCH_ALT_NO_SEQ = 0x6
ASSERT_PRIMARY = 0x8
ASSERT_ALTERNATE = 0x9
REPLACE_PRIMARY = 0xA
REPLACE_ALTERNATE = 0xB
UNDEFINE_PRIMARY = 0xC
UNDEFINE_ALTERNATE = 0xD
USN_PAGE_SIZE = 0x1000
USN_REASON_DATA_OVERWRITE = 0x00000001
USN_REASON_DATA_EXTEND = 0x00000002
USN_REASON_DATA_TRUNCATION = 0x00000004
USN_REASON_NAMED_DATA_OVERWRITE = 0x00000010
USN_REASON_NAMED_DATA_EXTEND = 0x00000020
USN_REASON_NAMED_DATA_TRUNCATION = 0x00000040
USN_REASON_FILE_CREATE = 0x00000100
USN_REASON_FILE_DELETE = 0x00000200
USN_REASON_EA_CHANGE = 0x00000400
USN_REASON_SECURITY_CHANGE = 0x00000800
USN_REASON_RENAME_OLD_NAME = 0x00001000
USN_REASON_RENAME_NEW_NAME = 0x00002000
USN_REASON_INDEXABLE_CHANGE = 0x00004000
USN_REASON_BASIC_INFO_CHANGE = 0x00008000
USN_REASON_HARD_LINK_CHANGE = 0x00010000
USN_REASON_COMPRESSION_CHANGE = 0x00020000
USN_REASON_ENCRYPTION_CHANGE = 0x00040000
USN_REASON_OBJECT_ID_CHANGE = 0x00080000
USN_REASON_REPARSE_POINT_CHANGE = 0x00100000
USN_REASON_STREAM_CHANGE = 0x00200000
USN_REASON_TRANSACTED_CHANGE = 0x00400000
USN_REASON_CLOSE = 0x80000000
USN_DELETE_FLAG_DELETE = 0x00000001
USN_DELETE_FLAG_NOTIFY = 0x00000002
USN_DELETE_VALID_FLAGS = 0x00000003
USN_SOURCE_DATA_MANAGEMENT = 0x00000001
USN_SOURCE_AUXILIARY_DATA = 0x00000002
USN_SOURCE_REPLICATION_MANAGEMENT = 0x00000004

MARK_HANDLE_PROTECT_CLUSTERS = 1
MARK_HANDLE_TXF_SYSTEM_LOG = 4
MARK_HANDLE_NOT_TXF_SYSTEM_LOG = 8

VOLUME_IS_DIRTY = 0x00000001
VOLUME_UPGRADE_SCHEDULED = 0x00000002
VOLUME_SESSION_OPEN = 4

FILE_PREFETCH_TYPE_FOR_CREATE = 1
FILE_PREFETCH_TYPE_FOR_DIRENUM = 2
FILE_PREFETCH_TYPE_FOR_CREATE_EX = 3
FILE_PREFETCH_TYPE_FOR_DIRENUM_EX = 4
FILE_PREFETCH_TYPE_MAX = 4

FILESYSTEM_STATISTICS_TYPE_NTFS = 1
FILESYSTEM_STATISTICS_TYPE_FAT = 2
FILE_SET_ENCRYPTION = 0x00000001
FILE_CLEAR_ENCRYPTION = 0x00000002
STREAM_SET_ENCRYPTION = 0x00000003
STREAM_CLEAR_ENCRYPTION = 0x00000004
MAXIMUM_ENCRYPTION_VALUE = 0x00000004
ENCRYPTION_FORMAT_DEFAULT = 0x01
COMPRESSION_FORMAT_SPARSE = 0x4000
COPYFILE_SIS_LINK = 0x0001
COPYFILE_SIS_REPLACE = 0x0002
COPYFILE_SIS_FLAGS = 0x0003

WMI_DISK_GEOMETRY_GUID = pywintypes.IID(
    "{25007F51-57C2-11D1-A528-00A0C9062910}")
GUID_DEVINTERFACE_CDROM = pywintypes.IID(
    "{53F56308-B6BF-11D0-94F2-00A0C91EFB8B}")
GUID_DEVINTERFACE_FLOPPY = pywintypes.IID(
    "{53F56311-B6BF-11D0-94F2-00A0C91EFB8B}")
GUID_DEVINTERFACE_SERENUM_BUS_ENUMERATOR = pywintypes.IID(
    "{4D36E978-E325-11CE-BFC1-08002BE10318}")
GUID_DEVINTERFACE_COMPORT = pywintypes.IID(
    "{86E0D1E0-8089-11D0-9CE4-08003E301F73}")
GUID_DEVINTERFACE_DISK = pywintypes.IID(
    "{53F56307-B6BF-11D0-94F2-00A0C91EFB8B}")
GUID_DEVINTERFACE_STORAGEPORT = pywintypes.IID(
    "{2ACCFE60-C130-11D2-B082-00A0C91EFB8B}")
GUID_DEVINTERFACE_CDCHANGER = pywintypes.IID(
    "{53F56312-B6BF-11D0-94F2-00A0C91EFB8B}")
GUID_DEVINTERFACE_PARTITION = pywintypes.IID(
    "{53F5630A-B6BF-11D0-94F2-00A0C91EFB8B}")
GUID_DEVINTERFACE_VOLUME = pywintypes.IID(
    "{53F5630D-B6BF-11D0-94F2-00A0C91EFB8B}")
GUID_DEVINTERFACE_WRITEONCEDISK = pywintypes.IID(
    "{53F5630C-B6BF-11D0-94F2-00A0C91EFB8B}")
GUID_DEVINTERFACE_TAPE = pywintypes.IID(
    "{53F5630B-B6BF-11D0-94F2-00A0C91EFB8B}")
GUID_DEVINTERFACE_MEDIUMCHANGER = pywintypes.IID(
    "{53F56310-B6BF-11D0-94F2-00A0C91EFB8B}")
GUID_SERENUM_BUS_ENUMERATOR = GUID_DEVINTERFACE_SERENUM_BUS_ENUMERATOR
GUID_CLASS_COMPORT = GUID_DEVINTERFACE_COMPORT

DiskClassGuid = GUID_DEVINTERFACE_DISK
CdRomClassGuid = GUID_DEVINTERFACE_CDROM
PartitionClassGuid = GUID_DEVINTERFACE_PARTITION
TapeClassGuid = GUID_DEVINTERFACE_TAPE
WriteOnceDiskClassGuid = GUID_DEVINTERFACE_WRITEONCEDISK
VolumeClassGuid = GUID_DEVINTERFACE_VOLUME
MediumChangerClassGuid = GUID_DEVINTERFACE_MEDIUMCHANGER
FloppyClassGuid = GUID_DEVINTERFACE_FLOPPY
CdChangerClassGuid = GUID_DEVINTERFACE_CDCHANGER
StoragePortClassGuid = GUID_DEVINTERFACE_STORAGEPORT


IOCTL_STORAGE_CHECK_VERIFY = CTL_CODE(
    IOCTL_STORAGE_BASE, 0x0200, METHOD_BUFFERED, FILE_READ_ACCESS)
IOCTL_STORAGE_CHECK_VERIFY2 = CTL_CODE(
    IOCTL_STORAGE_BASE, 0x0200, METHOD_BUFFERED, FILE_ANY_ACCESS)
IOCTL_STORAGE_MEDIA_REMOVAL = CTL_CODE(
    IOCTL_STORAGE_BASE, 0x0201, METHOD_BUFFERED, FILE_READ_ACCESS)
IOCTL_STORAGE_EJECT_MEDIA = CTL_CODE(
    IOCTL_STORAGE_BASE, 0x0202, METHOD_BUFFERED, FILE_READ_ACCESS)
IOCTL_STORAGE_LOAD_MEDIA = CTL_CODE(
    IOCTL_STORAGE_BASE, 0x0203, METHOD_BUFFERED, FILE_READ_ACCESS)
IOCTL_STORAGE_LOAD_MEDIA2 = CTL_CODE(
    IOCTL_STORAGE_BASE, 0x0203, METHOD_BUFFERED, FILE_ANY_ACCESS)
IOCTL_STORAGE_RESERVE = CTL_CODE(
    IOCTL_STORAGE_BASE, 0x0204, METHOD_BUFFERED, FILE_READ_ACCESS)
IOCTL_STORAGE_RELEASE = CTL_CODE(
    IOCTL_STORAGE_BASE, 0x0205, METHOD_BUFFERED, FILE_READ_ACCESS)
IOCTL_STORAGE_FIND_NEW_DEVICES = CTL_CODE(
    IOCTL_STORAGE_BASE, 0x0206, METHOD_BUFFERED, FILE_READ_ACCESS)
IOCTL_STORAGE_EJECTION_CONTROL = CTL_CODE(
    IOCTL_STORAGE_BASE, 0x0250, METHOD_BUFFERED, FILE_ANY_ACCESS)
IOCTL_STORAGE_MCN_CONTROL = CTL_CODE(
    IOCTL_STORAGE_BASE, 0x0251, METHOD_BUFFERED, FILE_ANY_ACCESS)
IOCTL_STORAGE_GET_MEDIA_TYPES = CTL_CODE(
    IOCTL_STORAGE_BASE, 0x0300, METHOD_BUFFERED, FILE_ANY_ACCESS)
IOCTL_STORAGE_GET_MEDIA_TYPES_EX = CTL_CODE(
    IOCTL_STORAGE_BASE, 0x0301, METHOD_BUFFERED, FILE_ANY_ACCESS)
IOCTL_STORAGE_GET_MEDIA_SERIAL_NUMBER = CTL_CODE(
    IOCTL_STORAGE_BASE, 0x0304, METHOD_BUFFERED, FILE_ANY_ACCESS)
IOCTL_STORAGE_GET_HOTPLUG_INFO = CTL_CODE(
    IOCTL_STORAGE_BASE, 0x0305, METHOD_BUFFERED, FILE_ANY_ACCESS)
IOCTL_STORAGE_SET_HOTPLUG_INFO = CTL_CODE(
    IOCTL_STORAGE_BASE, 0x0306, METHOD_BUFFERED, FILE_READ_ACCESS | FILE_WRITE_ACCESS)
IOCTL_STORAGE_RESET_BUS = CTL_CODE(
    IOCTL_STORAGE_BASE, 0x0400, METHOD_BUFFERED, FILE_READ_ACCESS)
IOCTL_STORAGE_RESET_DEVICE = CTL_CODE(
    IOCTL_STORAGE_BASE, 0x0401, METHOD_BUFFERED, FILE_READ_ACCESS)
IOCTL_STORAGE_BREAK_RESERVATION = CTL_CODE(
    IOCTL_STORAGE_BASE, 0x0405, METHOD_BUFFERED, FILE_READ_ACCESS)
IOCTL_STORAGE_GET_DEVICE_NUMBER = CTL_CODE(
    IOCTL_STORAGE_BASE, 0x0420, METHOD_BUFFERED, FILE_ANY_ACCESS)
IOCTL_STORAGE_PREDICT_FAILURE = CTL_CODE(
    IOCTL_STORAGE_BASE, 0x0440, METHOD_BUFFERED, FILE_ANY_ACCESS)
IOCTL_DISK_GET_DRIVE_GEOMETRY = CTL_CODE(
    IOCTL_DISK_BASE, 0x0000, METHOD_BUFFERED, FILE_ANY_ACCESS)
IOCTL_DISK_GET_PARTITION_INFO = CTL_CODE(
    IOCTL_DISK_BASE, 0x0001, METHOD_BUFFERED, FILE_READ_ACCESS)
IOCTL_DISK_SET_PARTITION_INFO = CTL_CODE(
    IOCTL_DISK_BASE, 0x0002, METHOD_BUFFERED, FILE_READ_ACCESS | FILE_WRITE_ACCESS)
IOCTL_DISK_GET_DRIVE_LAYOUT = CTL_CODE(
    IOCTL_DISK_BASE, 0x0003, METHOD_BUFFERED, FILE_READ_ACCESS)
IOCTL_DISK_SET_DRIVE_LAYOUT = CTL_CODE(
    IOCTL_DISK_BASE, 0x0004, METHOD_BUFFERED, FILE_READ_ACCESS | FILE_WRITE_ACCESS)
IOCTL_DISK_VERIFY = CTL_CODE(
    IOCTL_DISK_BASE, 0x0005, METHOD_BUFFERED, FILE_ANY_ACCESS)
IOCTL_DISK_FORMAT_TRACKS = CTL_CODE(
    IOCTL_DISK_BASE, 0x0006, METHOD_BUFFERED, FILE_READ_ACCESS | FILE_WRITE_ACCESS)
IOCTL_DISK_REASSIGN_BLOCKS = CTL_CODE(
    IOCTL_DISK_BASE, 0x0007, METHOD_BUFFERED, FILE_READ_ACCESS | FILE_WRITE_ACCESS)
IOCTL_DISK_PERFORMANCE = CTL_CODE(
    IOCTL_DISK_BASE, 0x0008, METHOD_BUFFERED, FILE_ANY_ACCESS)
IOCTL_DISK_IS_WRITABLE = CTL_CODE(
    IOCTL_DISK_BASE, 0x0009, METHOD_BUFFERED, FILE_ANY_ACCESS)
IOCTL_DISK_LOGGING = CTL_CODE(
    IOCTL_DISK_BASE, 0x000a, METHOD_BUFFERED, FILE_ANY_ACCESS)
IOCTL_DISK_FORMAT_TRACKS_EX = CTL_CODE(
    IOCTL_DISK_BASE, 0x000b, METHOD_BUFFERED, FILE_READ_ACCESS | FILE_WRITE_ACCESS)
IOCTL_DISK_HISTOGRAM_STRUCTURE = CTL_CODE(
    IOCTL_DISK_BASE, 0x000c, METHOD_BUFFERED, FILE_ANY_ACCESS)
IOCTL_DISK_HISTOGRAM_DATA = CTL_CODE(
    IOCTL_DISK_BASE, 0x000d, METHOD_BUFFERED, FILE_ANY_ACCESS)
IOCTL_DISK_HISTOGRAM_RESET = CTL_CODE(
    IOCTL_DISK_BASE, 0x000e, METHOD_BUFFERED, FILE_ANY_ACCESS)
IOCTL_DISK_REQUEST_STRUCTURE = CTL_CODE(
    IOCTL_DISK_BASE, 0x000f, METHOD_BUFFERED, FILE_ANY_ACCESS)
IOCTL_DISK_REQUEST_DATA = CTL_CODE(
    IOCTL_DISK_BASE, 0x0010, METHOD_BUFFERED, FILE_ANY_ACCESS)
IOCTL_DISK_PERFORMANCE_OFF = CTL_CODE(
    IOCTL_DISK_BASE, 0x0018, METHOD_BUFFERED, FILE_ANY_ACCESS)
IOCTL_DISK_CONTROLLER_NUMBER = CTL_CODE(
    IOCTL_DISK_BASE, 0x0011, METHOD_BUFFERED, FILE_ANY_ACCESS)
SMART_GET_VERSION = CTL_CODE(
    IOCTL_DISK_BASE, 0x0020, METHOD_BUFFERED, FILE_READ_ACCESS)
SMART_SEND_DRIVE_COMMAND = CTL_CODE(
    IOCTL_DISK_BASE, 0x0021, METHOD_BUFFERED, FILE_READ_ACCESS | FILE_WRITE_ACCESS)
SMART_RCV_DRIVE_DATA = CTL_CODE(
    IOCTL_DISK_BASE, 0x0022, METHOD_BUFFERED, FILE_READ_ACCESS | FILE_WRITE_ACCESS)
IOCTL_DISK_GET_PARTITION_INFO_EX = CTL_CODE(
    IOCTL_DISK_BASE, 0x0012, METHOD_BUFFERED, FILE_ANY_ACCESS)
IOCTL_DISK_SET_PARTITION_INFO_EX = CTL_CODE(
    IOCTL_DISK_BASE, 0x0013, METHOD_BUFFERED, FILE_READ_ACCESS | FILE_WRITE_ACCESS)
IOCTL_DISK_GET_DRIVE_LAYOUT_EX = CTL_CODE(
    IOCTL_DISK_BASE, 0x0014, METHOD_BUFFERED, FILE_ANY_ACCESS)
IOCTL_DISK_SET_DRIVE_LAYOUT_EX = CTL_CODE(
    IOCTL_DISK_BASE, 0x0015, METHOD_BUFFERED, FILE_READ_ACCESS | FILE_WRITE_ACCESS)
IOCTL_DISK_CREATE_DISK = CTL_CODE(
    IOCTL_DISK_BASE, 0x0016, METHOD_BUFFERED, FILE_READ_ACCESS | FILE_WRITE_ACCESS)
IOCTL_DISK_GET_LENGTH_INFO = CTL_CODE(
    IOCTL_DISK_BASE, 0x0017, METHOD_BUFFERED, FILE_READ_ACCESS)
IOCTL_DISK_GET_DRIVE_GEOMETRY_EX = CTL_CODE(
    IOCTL_DISK_BASE, 0x0028, METHOD_BUFFERED, FILE_ANY_ACCESS)
IOCTL_DISK_REASSIGN_BLOCKS_EX = CTL_CODE(
    IOCTL_DISK_BASE, 0x0029, METHOD_BUFFERED, FILE_READ_ACCESS | FILE_WRITE_ACCESS)

IOCTL_DISK_UPDATE_DRIVE_SIZE = CTL_CODE(
    IOCTL_DISK_BASE, 0x0032, METHOD_BUFFERED, FILE_READ_ACCESS | FILE_WRITE_ACCESS)
IOCTL_DISK_GROW_PARTITION = CTL_CODE(
    IOCTL_DISK_BASE, 0x0034, METHOD_BUFFERED, FILE_READ_ACCESS | FILE_WRITE_ACCESS)
IOCTL_DISK_GET_CACHE_INFORMATION = CTL_CODE(
    IOCTL_DISK_BASE, 0x0035, METHOD_BUFFERED, FILE_READ_ACCESS)
IOCTL_DISK_SET_CACHE_INFORMATION = CTL_CODE(
    IOCTL_DISK_BASE, 0x0036, METHOD_BUFFERED, FILE_READ_ACCESS | FILE_WRITE_ACCESS)

OBSOLETE_IOCTL_STORAGE_RESET_BUS = CTL_CODE(
    IOCTL_STORAGE_BASE, 0x0400, METHOD_BUFFERED, FILE_READ_ACCESS | FILE_WRITE_ACCESS)
OBSOLETE_IOCTL_STORAGE_RESET_DEVICE = CTL_CODE(
    IOCTL_STORAGE_BASE, 0x0401, METHOD_BUFFERED, FILE_READ_ACCESS | FILE_WRITE_ACCESS)
# the original define no longer exists in winioctl.h
OBSOLETE_DISK_GET_WRITE_CACHE_STATE = CTL_CODE(
    IOCTL_DISK_BASE, 0x0037, METHOD_BUFFERED, FILE_READ_ACCESS)
IOCTL_DISK_GET_WRITE_CACHE_STATE = OBSOLETE_DISK_GET_WRITE_CACHE_STATE


IOCTL_DISK_DELETE_DRIVE_LAYOUT = CTL_CODE(
    IOCTL_DISK_BASE, 0x0040, METHOD_BUFFERED, FILE_READ_ACCESS | FILE_WRITE_ACCESS)
IOCTL_DISK_UPDATE_PROPERTIES = CTL_CODE(
    IOCTL_DISK_BASE, 0x0050, METHOD_BUFFERED, FILE_ANY_ACCESS)
IOCTL_DISK_FORMAT_DRIVE = CTL_CODE(
    IOCTL_DISK_BASE, 0x00f3, METHOD_BUFFERED, FILE_READ_ACCESS | FILE_WRITE_ACCESS)
IOCTL_DISK_SENSE_DEVICE = CTL_CODE(
    IOCTL_DISK_BASE, 0x00f8, METHOD_BUFFERED, FILE_ANY_ACCESS)
IOCTL_DISK_CHECK_VERIFY = CTL_CODE(
    IOCTL_DISK_BASE, 0x0200, METHOD_BUFFERED, FILE_READ_ACCESS)
IOCTL_DISK_MEDIA_REMOVAL = CTL_CODE(
    IOCTL_DISK_BASE, 0x0201, METHOD_BUFFERED, FILE_READ_ACCESS)
IOCTL_DISK_EJECT_MEDIA = CTL_CODE(
    IOCTL_DISK_BASE, 0x0202, METHOD_BUFFERED, FILE_READ_ACCESS)
IOCTL_DISK_LOAD_MEDIA = CTL_CODE(
    IOCTL_DISK_BASE, 0x0203, METHOD_BUFFERED, FILE_READ_ACCESS)
IOCTL_DISK_RESERVE = CTL_CODE(
    IOCTL_DISK_BASE, 0x0204, METHOD_BUFFERED, FILE_READ_ACCESS)
IOCTL_DISK_RELEASE = CTL_CODE(
    IOCTL_DISK_BASE, 0x0205, METHOD_BUFFERED, FILE_READ_ACCESS)
IOCTL_DISK_FIND_NEW_DEVICES = CTL_CODE(
    IOCTL_DISK_BASE, 0x0206, METHOD_BUFFERED, FILE_READ_ACCESS)
IOCTL_DISK_GET_MEDIA_TYPES = CTL_CODE(
    IOCTL_DISK_BASE, 0x0300, METHOD_BUFFERED, FILE_ANY_ACCESS)

DISK_HISTOGRAM_SIZE = 72
HISTOGRAM_BUCKET_SIZE = 8

IOCTL_CHANGER_GET_PARAMETERS = CTL_CODE(
    IOCTL_CHANGER_BASE, 0x0000, METHOD_BUFFERED, FILE_READ_ACCESS)
IOCTL_CHANGER_GET_STATUS = CTL_CODE(
    IOCTL_CHANGER_BASE, 0x0001, METHOD_BUFFERED, FILE_READ_ACCESS)
IOCTL_CHANGER_GET_PRODUCT_DATA = CTL_CODE(
    IOCTL_CHANGER_BASE, 0x0002, METHOD_BUFFERED, FILE_READ_ACCESS)
IOCTL_CHANGER_SET_ACCESS = CTL_CODE(
    IOCTL_CHANGER_BASE, 0x0004, METHOD_BUFFERED, FILE_READ_ACCESS | FILE_WRITE_ACCESS)
IOCTL_CHANGER_GET_ELEMENT_STATUS = CTL_CODE(
    IOCTL_CHANGER_BASE, 0x0005, METHOD_BUFFERED, FILE_READ_ACCESS | FILE_WRITE_ACCESS)
IOCTL_CHANGER_INITIALIZE_ELEMENT_STATUS = CTL_CODE(
    IOCTL_CHANGER_BASE, 0x0006, METHOD_BUFFERED, FILE_READ_ACCESS)
IOCTL_CHANGER_SET_POSITION = CTL_CODE(
    IOCTL_CHANGER_BASE, 0x0007, METHOD_BUFFERED, FILE_READ_ACCESS)
IOCTL_CHANGER_EXCHANGE_MEDIUM = CTL_CODE(
    IOCTL_CHANGER_BASE, 0x0008, METHOD_BUFFERED, FILE_READ_ACCESS)
IOCTL_CHANGER_MOVE_MEDIUM = CTL_CODE(
    IOCTL_CHANGER_BASE, 0x0009, METHOD_BUFFERED, FILE_READ_ACCESS)
IOCTL_CHANGER_REINITIALIZE_TRANSPORT = CTL_CODE(
    IOCTL_CHANGER_BASE, 0x000A, METHOD_BUFFERED, FILE_READ_ACCESS)
IOCTL_CHANGER_QUERY_VOLUME_TAGS = CTL_CODE(
    IOCTL_CHANGER_BASE, 0x000B, METHOD_BUFFERED, FILE_READ_ACCESS | FILE_WRITE_ACCESS)
IOCTL_SERIAL_LSRMST_INSERT = CTL_CODE(
    FILE_DEVICE_SERIAL_PORT, 31, METHOD_BUFFERED, FILE_ANY_ACCESS)
IOCTL_SERENUM_EXPOSE_HARDWARE = CTL_CODE(
    FILE_DEVICE_SERENUM, 128, METHOD_BUFFERED, FILE_ANY_ACCESS)
IOCTL_SERENUM_REMOVE_HARDWARE = CTL_CODE(
    FILE_DEVICE_SERENUM, 129, METHOD_BUFFERED, FILE_ANY_ACCESS)
IOCTL_SERENUM_PORT_DESC = CTL_CODE(
    FILE_DEVICE_SERENUM, 130, METHOD_BUFFERED, FILE_ANY_ACCESS)
IOCTL_SERENUM_GET_PORT_NAME = CTL_CODE(
    FILE_DEVICE_SERENUM, 131, METHOD_BUFFERED, FILE_ANY_ACCESS)

# ??? can't find where FILE_DEVICE_AVIO is defined ???
## IOCTL_AVIO_ALLOCATE_STREAM = CTL_CODE(FILE_DEVICE_AVIO, 1, METHOD_BUFFERED, FILE_SPECIAL_ACCESS)
## IOCTL_AVIO_FREE_STREAM = CTL_CODE(FILE_DEVICE_AVIO, 2, METHOD_BUFFERED, FILE_SPECIAL_ACCESS)
## IOCTL_AVIO_MODIFY_STREAM = CTL_CODE(FILE_DEVICE_AVIO, 3, METHOD_BUFFERED, FILE_SPECIAL_ACCESS)

SERIAL_LSRMST_ESCAPE = 0x00
SERIAL_LSRMST_LSR_DATA = 0x01
SERIAL_LSRMST_LSR_NODATA = 0x02
SERIAL_LSRMST_MST = 0x03
SERIAL_IOC_FCR_FIFO_ENABLE = 0x00000001
SERIAL_IOC_FCR_RCVR_RESET = 0x00000002
SERIAL_IOC_FCR_XMIT_RESET = 0x00000004
SERIAL_IOC_FCR_DMA_MODE = 0x00000008
SERIAL_IOC_FCR_RES1 = 0x00000010
SERIAL_IOC_FCR_RES2 = 0x00000020
SERIAL_IOC_FCR_RCVR_TRIGGER_LSB = 0x00000040
SERIAL_IOC_FCR_RCVR_TRIGGER_MSB = 0x00000080
SERIAL_IOC_MCR_DTR = 0x00000001
SERIAL_IOC_MCR_RTS = 0x00000002
SERIAL_IOC_MCR_OUT1 = 0x00000004
SERIAL_IOC_MCR_OUT2 = 0x00000008
SERIAL_IOC_MCR_LOOP = 0x00000010
FSCTL_REQUEST_OPLOCK_LEVEL_1 = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM,  0, METHOD_BUFFERED, FILE_ANY_ACCESS)
FSCTL_REQUEST_OPLOCK_LEVEL_2 = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM,  1, METHOD_BUFFERED, FILE_ANY_ACCESS)
FSCTL_REQUEST_BATCH_OPLOCK = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM,  2, METHOD_BUFFERED, FILE_ANY_ACCESS)
FSCTL_OPLOCK_BREAK_ACKNOWLEDGE = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM,  3, METHOD_BUFFERED, FILE_ANY_ACCESS)
FSCTL_OPBATCH_ACK_CLOSE_PENDING = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM,  4, METHOD_BUFFERED, FILE_ANY_ACCESS)
FSCTL_OPLOCK_BREAK_NOTIFY = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM,  5, METHOD_BUFFERED, FILE_ANY_ACCESS)
FSCTL_LOCK_VOLUME = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM,  6, METHOD_BUFFERED, FILE_ANY_ACCESS)
FSCTL_UNLOCK_VOLUME = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM,  7, METHOD_BUFFERED, FILE_ANY_ACCESS)
FSCTL_DISMOUNT_VOLUME = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM,  8, METHOD_BUFFERED, FILE_ANY_ACCESS)
FSCTL_IS_VOLUME_MOUNTED = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM, 10, METHOD_BUFFERED, FILE_ANY_ACCESS)
FSCTL_IS_PATHNAME_VALID = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM, 11, METHOD_BUFFERED, FILE_ANY_ACCESS)
FSCTL_MARK_VOLUME_DIRTY = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM, 12, METHOD_BUFFERED, FILE_ANY_ACCESS)
FSCTL_QUERY_RETRIEVAL_POINTERS = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM, 14,  METHOD_NEITHER, FILE_ANY_ACCESS)
FSCTL_GET_COMPRESSION = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM, 15, METHOD_BUFFERED, FILE_ANY_ACCESS)
FSCTL_SET_COMPRESSION = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM, 16, METHOD_BUFFERED, FILE_READ_DATA | FILE_WRITE_DATA)
FSCTL_MARK_AS_SYSTEM_HIVE = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM, 19,  METHOD_NEITHER, FILE_ANY_ACCESS)
FSCTL_OPLOCK_BREAK_ACK_NO_2 = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM, 20, METHOD_BUFFERED, FILE_ANY_ACCESS)
FSCTL_INVALIDATE_VOLUMES = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM, 21, METHOD_BUFFERED, FILE_ANY_ACCESS)
FSCTL_QUERY_FAT_BPB = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM, 22, METHOD_BUFFERED, FILE_ANY_ACCESS)
FSCTL_REQUEST_FILTER_OPLOCK = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM, 23, METHOD_BUFFERED, FILE_ANY_ACCESS)
FSCTL_FILESYSTEM_GET_STATISTICS = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM, 24, METHOD_BUFFERED, FILE_ANY_ACCESS)
FSCTL_GET_NTFS_VOLUME_DATA = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM, 25, METHOD_BUFFERED, FILE_ANY_ACCESS)
FSCTL_GET_NTFS_FILE_RECORD = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM, 26, METHOD_BUFFERED, FILE_ANY_ACCESS)
FSCTL_GET_VOLUME_BITMAP = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM, 27,  METHOD_NEITHER, FILE_ANY_ACCESS)
FSCTL_GET_RETRIEVAL_POINTERS = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM, 28,  METHOD_NEITHER, FILE_ANY_ACCESS)
FSCTL_MOVE_FILE = CTL_CODE(FILE_DEVICE_FILE_SYSTEM,
                           29, METHOD_BUFFERED, FILE_SPECIAL_ACCESS)
FSCTL_IS_VOLUME_DIRTY = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM, 30, METHOD_BUFFERED, FILE_ANY_ACCESS)
FSCTL_ALLOW_EXTENDED_DASD_IO = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM, 32, METHOD_NEITHER,  FILE_ANY_ACCESS)
FSCTL_FIND_FILES_BY_SID = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM, 35, METHOD_NEITHER, FILE_ANY_ACCESS)
FSCTL_SET_OBJECT_ID = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM, 38, METHOD_BUFFERED, FILE_SPECIAL_ACCESS)
FSCTL_GET_OBJECT_ID = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM, 39, METHOD_BUFFERED, FILE_ANY_ACCESS)
FSCTL_DELETE_OBJECT_ID = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM, 40, METHOD_BUFFERED, FILE_SPECIAL_ACCESS)
FSCTL_SET_REPARSE_POINT = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM, 41, METHOD_BUFFERED, FILE_SPECIAL_ACCESS)
FSCTL_GET_REPARSE_POINT = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM, 42, METHOD_BUFFERED, FILE_ANY_ACCESS)
FSCTL_DELETE_REPARSE_POINT = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM, 43, METHOD_BUFFERED, FILE_SPECIAL_ACCESS)
FSCTL_ENUM_USN_DATA = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM, 44,  METHOD_NEITHER, FILE_ANY_ACCESS)
FSCTL_SECURITY_ID_CHECK = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM, 45,  METHOD_NEITHER, FILE_READ_DATA)
FSCTL_READ_USN_JOURNAL = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM, 46,  METHOD_NEITHER, FILE_ANY_ACCESS)
FSCTL_SET_OBJECT_ID_EXTENDED = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM, 47, METHOD_BUFFERED, FILE_SPECIAL_ACCESS)
FSCTL_CREATE_OR_GET_OBJECT_ID = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM, 48, METHOD_BUFFERED, FILE_ANY_ACCESS)
FSCTL_SET_SPARSE = CTL_CODE(FILE_DEVICE_FILE_SYSTEM,
                            49, METHOD_BUFFERED, FILE_SPECIAL_ACCESS)
FSCTL_SET_ZERO_DATA = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM, 50, METHOD_BUFFERED, FILE_WRITE_DATA)
FSCTL_QUERY_ALLOCATED_RANGES = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM, 51,  METHOD_NEITHER, FILE_READ_DATA)
FSCTL_SET_ENCRYPTION = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM, 53,  METHOD_NEITHER, FILE_ANY_ACCESS)
FSCTL_ENCRYPTION_FSCTL_IO = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM, 54,  METHOD_NEITHER, FILE_ANY_ACCESS)
FSCTL_WRITE_RAW_ENCRYPTED = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM, 55,  METHOD_NEITHER, FILE_SPECIAL_ACCESS)
FSCTL_READ_RAW_ENCRYPTED = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM, 56,  METHOD_NEITHER, FILE_SPECIAL_ACCESS)
FSCTL_CREATE_USN_JOURNAL = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM, 57,  METHOD_NEITHER, FILE_ANY_ACCESS)
FSCTL_READ_FILE_USN_DATA = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM, 58,  METHOD_NEITHER, FILE_ANY_ACCESS)
FSCTL_WRITE_USN_CLOSE_RECORD = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM, 59,  METHOD_NEITHER, FILE_ANY_ACCESS)
FSCTL_EXTEND_VOLUME = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM, 60, METHOD_BUFFERED, FILE_ANY_ACCESS)
FSCTL_QUERY_USN_JOURNAL = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM, 61, METHOD_BUFFERED, FILE_ANY_ACCESS)
FSCTL_DELETE_USN_JOURNAL = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM, 62, METHOD_BUFFERED, FILE_ANY_ACCESS)
FSCTL_MARK_HANDLE = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM, 63, METHOD_BUFFERED, FILE_ANY_ACCESS)
FSCTL_SIS_COPYFILE = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM, 64, METHOD_BUFFERED, FILE_ANY_ACCESS)
FSCTL_SIS_LINK_FILES = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM, 65, METHOD_BUFFERED, FILE_READ_DATA | FILE_WRITE_DATA)
FSCTL_HSM_MSG = CTL_CODE(FILE_DEVICE_FILE_SYSTEM, 66,
                         METHOD_BUFFERED, FILE_READ_DATA | FILE_WRITE_DATA)
FSCTL_HSM_DATA = CTL_CODE(FILE_DEVICE_FILE_SYSTEM, 68,
                          METHOD_NEITHER, FILE_READ_DATA | FILE_WRITE_DATA)
FSCTL_RECALL_FILE = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM, 69, METHOD_NEITHER, FILE_ANY_ACCESS)
FSCTL_READ_FROM_PLEX = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM, 71, METHOD_OUT_DIRECT, FILE_READ_DATA)
FSCTL_FILE_PREFETCH = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM, 72, METHOD_BUFFERED, FILE_SPECIAL_ACCESS)
FSCTL_MAKE_MEDIA_COMPATIBLE = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM, 76, METHOD_BUFFERED, FILE_WRITE_DATA)
FSCTL_SET_DEFECT_MANAGEMENT = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM, 77, METHOD_BUFFERED, FILE_WRITE_DATA)
FSCTL_QUERY_SPARING_INFO = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM, 78, METHOD_BUFFERED, FILE_ANY_ACCESS)
FSCTL_QUERY_ON_DISK_VOLUME_INFO = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM, 79, METHOD_BUFFERED, FILE_ANY_ACCESS)
FSCTL_SET_VOLUME_COMPRESSION_STATE = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM, 80, METHOD_BUFFERED, FILE_SPECIAL_ACCESS)
FSCTL_TXFS_MODIFY_RM = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM, 81, METHOD_BUFFERED, FILE_WRITE_DATA)
FSCTL_TXFS_QUERY_RM_INFORMATION = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM, 82, METHOD_BUFFERED, FILE_READ_DATA)
FSCTL_TXFS_ROLLFORWARD_REDO = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM, 84, METHOD_BUFFERED, FILE_WRITE_DATA)
FSCTL_TXFS_ROLLFORWARD_UNDO = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM, 85, METHOD_BUFFERED, FILE_WRITE_DATA)
FSCTL_TXFS_START_RM = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM, 86, METHOD_BUFFERED, FILE_WRITE_DATA)
FSCTL_TXFS_SHUTDOWN_RM = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM, 87, METHOD_BUFFERED, FILE_WRITE_DATA)
FSCTL_TXFS_READ_BACKUP_INFORMATION = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM, 88, METHOD_BUFFERED, FILE_READ_DATA)
FSCTL_TXFS_WRITE_BACKUP_INFORMATION = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM, 89, METHOD_BUFFERED, FILE_WRITE_DATA)
FSCTL_TXFS_CREATE_SECONDARY_RM = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM, 90, METHOD_BUFFERED, FILE_WRITE_DATA)
FSCTL_TXFS_GET_METADATA_INFO = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM, 91, METHOD_BUFFERED, FILE_READ_DATA)
FSCTL_TXFS_GET_TRANSACTED_VERSION = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM, 92, METHOD_BUFFERED, FILE_READ_DATA)
FSCTL_TXFS_CREATE_MINIVERSION = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM, 95, METHOD_BUFFERED, FILE_WRITE_DATA)
FSCTL_TXFS_TRANSACTION_ACTIVE = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM, 99, METHOD_BUFFERED, FILE_READ_DATA)
FSCTL_SET_ZERO_ON_DEALLOCATION = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM, 101, METHOD_BUFFERED, FILE_SPECIAL_ACCESS)
FSCTL_SET_REPAIR = CTL_CODE(FILE_DEVICE_FILE_SYSTEM,
                            102, METHOD_BUFFERED, FILE_ANY_ACCESS)
FSCTL_GET_REPAIR = CTL_CODE(FILE_DEVICE_FILE_SYSTEM,
                            103, METHOD_BUFFERED, FILE_ANY_ACCESS)
FSCTL_WAIT_FOR_REPAIR = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM, 104, METHOD_BUFFERED, FILE_ANY_ACCESS)
FSCTL_INITIATE_REPAIR = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM, 106, METHOD_BUFFERED, FILE_ANY_ACCESS)
FSCTL_CSC_INTERNAL = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM, 107, METHOD_NEITHER, FILE_ANY_ACCESS)
FSCTL_SHRINK_VOLUME = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM, 108, METHOD_BUFFERED, FILE_SPECIAL_ACCESS)
FSCTL_SET_SHORT_NAME_BEHAVIOR = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM, 109, METHOD_BUFFERED, FILE_ANY_ACCESS)
FSCTL_DFSR_SET_GHOST_HANDLE_STATE = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM, 110, METHOD_BUFFERED, FILE_ANY_ACCESS)
FSCTL_TXFS_LIST_TRANSACTION_LOCKED_FILES = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM, 120, METHOD_BUFFERED, FILE_READ_DATA)
FSCTL_TXFS_LIST_TRANSACTIONS = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM, 121, METHOD_BUFFERED, FILE_READ_DATA)
FSCTL_QUERY_PAGEFILE_ENCRYPTION = CTL_CODE(
    FILE_DEVICE_FILE_SYSTEM, 122, METHOD_BUFFERED, FILE_ANY_ACCESS)

IOCTL_VOLUME_BASE = ord('V')
IOCTL_VOLUME_GET_VOLUME_DISK_EXTENTS = CTL_CODE(
    IOCTL_VOLUME_BASE, 0, METHOD_BUFFERED, FILE_ANY_ACCESS)
IOCTL_VOLUME_ONLINE = CTL_CODE(
    IOCTL_VOLUME_BASE, 2, METHOD_BUFFERED, FILE_READ_ACCESS | FILE_WRITE_ACCESS)
IOCTL_VOLUME_OFFLINE = CTL_CODE(
    IOCTL_VOLUME_BASE, 3, METHOD_BUFFERED, FILE_READ_ACCESS | FILE_WRITE_ACCESS)
IOCTL_VOLUME_IS_CLUSTERED = CTL_CODE(
    IOCTL_VOLUME_BASE, 12, METHOD_BUFFERED, FILE_ANY_ACCESS)
IOCTL_VOLUME_GET_GPT_ATTRIBUTES = CTL_CODE(
    IOCTL_VOLUME_BASE, 14, METHOD_BUFFERED, FILE_ANY_ACCESS)

# enums
# STORAGE_MEDIA_TYPE
DDS_4mm = 32
MiniQic = 33
Travan = 34
QIC = 35
MP_8mm = 36
AME_8mm = 37
AIT1_8mm = 38
DLT = 39
NCTP = 40
IBM_3480 = 41
IBM_3490E = 42
IBM_Magstar_3590 = 43
IBM_Magstar_MP = 44
STK_DATA_D3 = 45
SONY_DTF = 46
DV_6mm = 47
DMI = 48
SONY_D2 = 49
CLEANER_CARTRIDGE = 50
CD_ROM = 51
CD_R = 52
CD_RW = 53
DVD_ROM = 54
DVD_R = 55
DVD_RW = 56
MO_3_RW = 57
MO_5_WO = 58
MO_5_RW = 59
MO_5_LIMDOW = 60
PC_5_WO = 61
PC_5_RW = 62
PD_5_RW = 63
ABL_5_WO = 64
PINNACLE_APEX_5_RW = 65
SONY_12_WO = 66
PHILIPS_12_WO = 67
HITACHI_12_WO = 68
CYGNET_12_WO = 69
KODAK_14_WO = 70
MO_NFR_525 = 71
NIKON_12_RW = 72
IOMEGA_ZIP = 73
IOMEGA_JAZ = 74
SYQUEST_EZ135 = 75
SYQUEST_EZFLYER = 76
SYQUEST_SYJET = 77
AVATAR_F2 = 78
MP2_8mm = 79
DST_S = 80
DST_M = 81
DST_L = 82
VXATape_1 = 83
VXATape_2 = 84
STK_9840 = 85
LTO_Ultrium = 86
LTO_Accelis = 87
DVD_RAM = 88
AIT_8mm = 89
ADR_1 = 90
ADR_2 = 91
STK_9940 = 92

# STORAGE_BUS_TYPE
BusTypeUnknown = 0
BusTypeScsi = 1
BusTypeAtapi = 2
BusTypeAta = 3
BusType1394 = 4
BusTypeSsa = 5
BusTypeFibre = 6
BusTypeUsb = 7
BusTypeRAID = 8
BusTypeiScsi = 9
BusTypeSas = 10
BusTypeSata = 11
BusTypeMaxReserved = 127

# MEDIA_TYPE
Unknown = 0
F5_1Pt2_512 = 1
F3_1Pt44_512 = 2
F3_2Pt88_512 = 3
F3_20Pt8_512 = 4
F3_720_512 = 5
F5_360_512 = 6
F5_320_512 = 7
F5_320_1024 = 8
F5_180_512 = 9
F5_160_512 = 10
RemovableMedia = 11
FixedMedia = 12
F3_120M_512 = 13
F3_640_512 = 14
F5_640_512 = 15
F5_720_512 = 16
F3_1Pt2_512 = 17
F3_1Pt23_1024 = 18
F5_1Pt23_1024 = 19
F3_128Mb_512 = 20
F3_230Mb_512 = 21
F8_256_128 = 22
F3_200Mb_512 = 23
F3_240M_512 = 24
F3_32M_512 = 25

# PARTITION_STYLE
PARTITION_STYLE_MBR = 0
PARTITION_STYLE_GPT = 1
PARTITION_STYLE_RAW = 2

# DETECTION_TYPE
DetectNone = 0
DetectInt13 = 1
DetectExInt13 = 2

# DISK_CACHE_RETENTION_PRIORITY
EqualPriority = 0
KeepPrefetchedData = 1
KeepReadData = 2

# DISK_WRITE_CACHE_STATE - ?????? this enum has disappeared from winioctl.h in windows 2003 SP1 sdk ??????
DiskWriteCacheNormal = 0
DiskWriteCacheForceDisable = 1
DiskWriteCacheDisableNotSupported = 2

# BIN_TYPES
RequestSize = 0
RequestLocation = 1

# CHANGER_DEVICE_PROBLEM_TYPE
DeviceProblemNone = 0
DeviceProblemHardware = 1
DeviceProblemCHMError = 2
DeviceProblemDoorOpen = 3
DeviceProblemCalibrationError = 4
DeviceProblemTargetFailure = 5
DeviceProblemCHMMoveError = 6
DeviceProblemCHMZeroError = 7
DeviceProblemCartridgeInsertError = 8
DeviceProblemPositionError = 9
DeviceProblemSensorError = 10
DeviceProblemCartridgeEjectError = 11
DeviceProblemGripperError = 12
DeviceProblemDriveError = 13
