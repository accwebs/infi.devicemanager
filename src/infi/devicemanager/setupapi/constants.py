
#TODO get real values of constants

def signed_hex_64(n):
    return (n & 0x7fffffff) | -(n & 0x80000000)

INVALID_HANDLE_VALUE = 0

DIGCF_DEFAULT = 1
DIGCF_PRESENT = 2
DIGCF_ALLCLASSES = 4
DIGCF_PROFILE = 8
DIGCF_DEVICEINTERFACE = 10

DIOD_INHERIT_CLASSDRVS = 2

DICS_FLAG_GLOBAL = 1
DICS_FLAG_CONFIGSPECIFIC = 2
DICS_FLAG_CONFIGGENERAL = 4

DIREG_DEV = 1
DIREG_DRV = 2
DIREG_BOTH = 4

GENDISK_GUID_STRING = "4D36E967-E325-11CE-BFC1-08002BE10318"
SCSIADAPTER_GUID_STRING = "4D36E97B-E325-11CE-BFC1-08002BE10318"
SYSTEM_DEVICE_GUID_STRING = "4D36E97D-E325-11CE-BFC1-08002BE10318"
GENVOLUME_GUID_STRING = "71A27CDD-812A-11D0-BEC7-08002BE2092F"

APPLICATION_ERROR_MASK = signed_hex_64(0x20000000)
ERROR_SEVERITY_SUCCESS = signed_hex_64(0x00000000)
ERROR_SEVERITY_INFORMATIONAL = signed_hex_64(0x40000000)
ERROR_SEVERITY_WARNING = signed_hex_64(0x80000000)
ERROR_SEVERITY_ERROR = signed_hex_64(0xC0000000)

ERROR_SUCCESS = 0
ERROR_FILE_NOT_FOUND = 2
ERROR_NO_MORE_ITEMS = 259
ERROR_BAD_COMMAND = 22
ERROR_INSUFFICIENT_BUFFER = 122
ERROR_INVALID_FLAGS = 1004
ERROR_INVALID_HANDLE = 6
ERROR_INVALID_DATA = 13
ERROR_INVALID_USER_BUFFER = 1784
ERROR_NO_SUCH_DEVINST = APPLICATION_ERROR_MASK|ERROR_SEVERITY_ERROR|signed_hex_64(0x20B)
ERROR_NOT_ENOUGH_MEMORY = 9
ERROR_NOT_FOUND = 1168
SDDL_REVISION_1 = 1

GENERIC_READ = signed_hex_64(0x80000000)
GENERIC_WRITE = signed_hex_64(0x40000000)
GENERIC_EXECUTE = signed_hex_64(0x20000000)
GENERIC_ALL = signed_hex_64(0x10000000)

FILE_SHARE_READ = signed_hex_64(0x00000001)
FILE_SHARE_WRITE = signed_hex_64(0x00000002)
FILE_SHARE_NONE = signed_hex_64(0x00000000)
FILE_SHARE_DELETE = signed_hex_64(0x00000004)

CREATE_NEW = 1
CREATE_ALWAYS = 2
OPEN_EXISTING = 3
OPEN_ALWAYS = 4
TRUNCATE_EXISTING = 5

FILE_FLAG_OVERLAPPED = signed_hex_64(0x40000000)

IOCTL_SCSI_GET_ADDRESS = 266264
IOCTL_STORAGE_GET_DEVICE_NUMBER = 2953344


DNF_MADEUP = signed_hex_64(0x00000001)
# The device was created and is owned by the PnP Manager. It was not created by a bus driver.
DNF_DUPLICATE = signed_hex_64(0x00000002)
# The device node is a duplicate of another enumerated device node.
DNF_HAL_NODE = signed_hex_64(0x00000004)
# The device node is the root node created by the hardware abstraction layer = HAL.
DNF_REENUMERATE = signed_hex_64(0x00000008)
# The device needs to be re-enumerated.
DNF_ENUMERATED = signed_hex_64(0x00000010)
# The PDO for the device was exposed by its parent.
DNF_IDS_QUERIED = signed_hex_64(0x00000020)
# The operating system should send IRP_MN_QUERY_ID requests to the device driver.
DNF_HAS_BOOT_CONFIG = signed_hex_64(0x00000040)
# The device has resources assigned by the BIOS. The device is considered pseudo-started and needs to participate in rebalancing.
DNF_BOOT_CONFIG_RESERVED = signed_hex_64(0x00000080)
# The boot resources of the device are reserved.
DNF_NO_RESOURCE_REQUIRED = signed_hex_64(0x00000100)
# The device does not require resources.
DNF_RESOURCE_REQUIREMENTS_NEED_FILTERED = signed_hex_64(0x00000200)
# The device's resource requirements list is a filtered list.
DNF_RESOURCE_REQUIREMENTS_CHANGED = signed_hex_64(0x00000400)
# The device's resource requirements list has changed.
DNF_NON_STOPPED_REBALANCE = signed_hex_64(0x00000800)
# The device can be restarted with new resources without being stopped.
DNF_LEGACY_DRIVER = signed_hex_64(0x00001000)
# The device's controlling driver is a non-PnP driver.
DNF_HAS_PROBLEM = signed_hex_64(0x00002000)
# The device has a problem and will be removed.
DNF_HAS_PRIVATE_PROBLEM = signed_hex_64(0x00004000)
# The device reported PNP_DEVICE_FAILED without also reporting PNP_DEVICE_RESOURCE_REQUIREMENTS_CHANGED.
DNF_HARDWARE_VERIFICATION = signed_hex_64(0x00008000)
# The device node has hardware verification.
DNF_DEVICE_GONE = signed_hex_64(0x00010000)
# The device's PDO is no longer returned in an IRP_QUERY_RELATIONS request.
DNF_LEGACY_RESOURCE_DEVICENODE = signed_hex_64(0x00020000)
# The device node was created for legacy resource allocation.
DNF_NEEDS_REBALANCE = signed_hex_64(0x00040000)
# The device node has triggered rebalancing.
DNF_LOCKED_FOR_EJECT = signed_hex_64(0x00080000)
# The device is being ejected or is related to a device that is being ejected.
DNF_DRIVER_BLOCKED = signed_hex_64(0x00100000)
# One or more of the drivers for the device node have been blocked from loading.
DNF_CHILD_WITH_INVALID_ID = signed_hex_64(0x00200000)
# One or more children of the device node have invalid IDs.
DNF_ASYNC_START_NOT_SUPPORTED = signed_hex_64(0x00400000)
# The device does not support asynchronous starts.
DNF_ASYNC_ENUMERATION_NOT_SUPPORTED = signed_hex_64(0x00800000)
# The device does not support asynchronous enumeration.
DNF_LOCKED_FOR_REBALANCE = signed_hex_64(0x01000000)
# The device is locked for rebalancing.
DNF_UNINSTALLED = signed_hex_64(0x02000000)
# An IRP_MN_QUERY_REMOVE_DEVICE request is in progress for the device.
DNF_NO_LOWER_DEVICE_FILTERS = signed_hex_64(0x04000000)
# There is no Registry entry of the lower-device-filters type for the device.
DNF_NO_LOWER_CLASS_FILTERS = signed_hex_64(0x08000000)
# There is no Registry entry of the lower-class-filters type for the device.
DNF_NO_SERVICE = signed_hex_64(0x10000000)
# There is no Registry entry of the service the for the device.
DNF_NO_UPPER_DEVICE_FILTERS = signed_hex_64(0x20000000)
# There is no Registry entry of the upper-device-filters type for the device.
DNF_NO_UPPER_CLASS_FILTERS = signed_hex_64(0x40000000)
# There is no Registry entry of the upper-class-filters type for the device.
DNF_WAITING_FOR_FDO = signed_hex_64(0x80000000)
# Enumeration of the device is waiting until the driver attaches its FDO.


DN_ROOT_ENUMERATED = signed_hex_64(0x1) # Was enumerated by ROOT
DN_DRIVER_LOADED = signed_hex_64(0x2) # Has Register_Device_Driver
DN_ENUM_LOADED = signed_hex_64(0x4) # Has Register_Enumerator
DN_STARTED = signed_hex_64(0x8) # Is currently configured
DN_MANUAL = signed_hex_64(0x10) # Manually installed
DN_NEED_TO_ENUM = signed_hex_64(0x20) # May need reenumeration
DN_NOT_FIRST_TIME = signed_hex_64(0x40) # Has received a config
DN_HARDWARE_ENUM = signed_hex_64(0x80) # Enum generates hardware ID
DN_LIAR = signed_hex_64(0x100) # Lied about can reconfig once
DN_HAS_MARK = signed_hex_64(0x200) # Not CM_Create_DevInst lately
DN_HAS_PROBLEM = signed_hex_64(0x400) # Need device installer
DN_FILTERED = signed_hex_64(0x800) # Is filtered
DN_MOVED = signed_hex_64(0x1000) # Has been moved
DN_DISABLEABLE = signed_hex_64(0x2000) # Can be disabled
DN_REMOVABLE = signed_hex_64(0x4000) # Can be removed
DN_PRIVATE_PROBLEM = signed_hex_64(0x8000) # Has a private problem
DN_MF_PARENT = signed_hex_64(0x10000) # Multi function parent
DN_MF_CHILD = signed_hex_64(0x20000) # Multi function child
DN_WILL_BE_REMOVED = signed_hex_64(0x40000) # DevInst is being removed
DN_NOT_FIRST_TIMEE = signed_hex_64(0x80000) # Has received a config enumerate
DN_STOP_FREE_RES = signed_hex_64(0x100000) # When child is stopped, free resources
DN_REBAL_CANDIDATE = signed_hex_64(0x200000) # Don't skip during rebalance
DN_BAD_PARTIAL = signed_hex_64(0x400000) # This devnode's log_confs do not have same resources
DN_NT_ENUMERATOR = signed_hex_64(0x800000) # This devnode's is an NT enumerator
DN_NT_DRIVER = signed_hex_64(0x1000000) # This devnode's is an NT driver
DN_NEEDS_LOCKING = signed_hex_64(0x2000000) # Devnode need lock resume processing
DN_ARM_WAKEUP = signed_hex_64(0x4000000) # Devnode can be the wakeup device
DN_APM_ENUMERATOR = signed_hex_64(0x8000000) # APM aware enumerator
DN_APM_DRIVER = signed_hex_64(0x10000000) # APM aware driver
DN_SILENT_INSTALL = signed_hex_64(0x20000000) # Silent install
DN_NO_SHOW_IN_DM = signed_hex_64(0x40000000) # No show in device manager
DN_BOOT_LOG_PROB = signed_hex_64(0x80000000) # Had a problem during preassignment of boot log conf
