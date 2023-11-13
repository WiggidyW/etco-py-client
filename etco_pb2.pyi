from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ErrorCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    OK: _ClassVar[ErrorCode]
    SERVER_ERROR: _ClassVar[ErrorCode]
    INVALID_REQUEST: _ClassVar[ErrorCode]
    INVALID_MERGE: _ClassVar[ErrorCode]
    BOOTSTRAP_UNSET: _ClassVar[ErrorCode]

class ContractStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    unknown_status: _ClassVar[ContractStatus]
    outstanding: _ClassVar[ContractStatus]
    in_progress: _ClassVar[ContractStatus]
    finished_issuer: _ClassVar[ContractStatus]
    finished_contractor: _ClassVar[ContractStatus]
    finished: _ClassVar[ContractStatus]
    cancelled: _ClassVar[ContractStatus]
    rejected: _ClassVar[ContractStatus]
    failed: _ClassVar[ContractStatus]
    deleted: _ClassVar[ContractStatus]
    reversed: _ClassVar[ContractStatus]

class ContractAssigneeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    unknown_assignee_type: _ClassVar[ContractAssigneeType]
    corporation: _ClassVar[ContractAssigneeType]
    character: _ClassVar[ContractAssigneeType]
    alliance: _ClassVar[ContractAssigneeType]

class MakePurchaseStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    MPS_SUCCESS: _ClassVar[MakePurchaseStatus]
    MPS_COOLDOWN_LIMIT: _ClassVar[MakePurchaseStatus]
    MPS_MAX_ACTIVE_LIMIT: _ClassVar[MakePurchaseStatus]
    MPS_ITEMS_REJECTED: _ClassVar[MakePurchaseStatus]
    MPS_ITEMS_UNAVAILABLE: _ClassVar[MakePurchaseStatus]
    MPS_ITEMS_REJECTED_AND_UNAVAILABLE: _ClassVar[MakePurchaseStatus]

class CancelPurchaseStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    CPS_SUCCESS: _ClassVar[CancelPurchaseStatus]
    CPS_COOLDOWN_LIMIT: _ClassVar[CancelPurchaseStatus]
    CPS_NOT_FOUND: _ClassVar[CancelPurchaseStatus]
    CPS_COOLDOWN_LIMIT_AND_NOT_FOUND: _ClassVar[CancelPurchaseStatus]
    CPS_NOT_ACTIVE: _ClassVar[CancelPurchaseStatus]

class EsiApp(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    EA_AUTH: _ClassVar[EsiApp]
    EA_MARKETS: _ClassVar[EsiApp]
    EA_CORPORATION: _ClassVar[EsiApp]
    EA_STRUCTURE_INFO: _ClassVar[EsiApp]
OK: ErrorCode
SERVER_ERROR: ErrorCode
INVALID_REQUEST: ErrorCode
INVALID_MERGE: ErrorCode
BOOTSTRAP_UNSET: ErrorCode
unknown_status: ContractStatus
outstanding: ContractStatus
in_progress: ContractStatus
finished_issuer: ContractStatus
finished_contractor: ContractStatus
finished: ContractStatus
cancelled: ContractStatus
rejected: ContractStatus
failed: ContractStatus
deleted: ContractStatus
reversed: ContractStatus
unknown_assignee_type: ContractAssigneeType
corporation: ContractAssigneeType
character: ContractAssigneeType
alliance: ContractAssigneeType
MPS_SUCCESS: MakePurchaseStatus
MPS_COOLDOWN_LIMIT: MakePurchaseStatus
MPS_MAX_ACTIVE_LIMIT: MakePurchaseStatus
MPS_ITEMS_REJECTED: MakePurchaseStatus
MPS_ITEMS_UNAVAILABLE: MakePurchaseStatus
MPS_ITEMS_REJECTED_AND_UNAVAILABLE: MakePurchaseStatus
CPS_SUCCESS: CancelPurchaseStatus
CPS_COOLDOWN_LIMIT: CancelPurchaseStatus
CPS_NOT_FOUND: CancelPurchaseStatus
CPS_COOLDOWN_LIMIT_AND_NOT_FOUND: CancelPurchaseStatus
CPS_NOT_ACTIVE: CancelPurchaseStatus
EA_AUTH: EsiApp
EA_MARKETS: EsiApp
EA_CORPORATION: EsiApp
EA_STRUCTURE_INFO: EsiApp

class OptionalInt32(_message.Message):
    __slots__ = ["inner"]
    INNER_FIELD_NUMBER: _ClassVar[int]
    inner: int
    def __init__(self, inner: _Optional[int] = ...) -> None: ...

class AuthRequest(_message.Message):
    __slots__ = ["token"]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: str
    def __init__(self, token: _Optional[str] = ...) -> None: ...

class AuthResponse(_message.Message):
    __slots__ = ["token", "authorized"]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZED_FIELD_NUMBER: _ClassVar[int]
    token: str
    authorized: bool
    def __init__(self, token: _Optional[str] = ..., authorized: bool = ...) -> None: ...

class ErrorResponse(_message.Message):
    __slots__ = ["error", "code"]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    error: str
    code: ErrorCode
    def __init__(self, error: _Optional[str] = ..., code: _Optional[_Union[ErrorCode, str]] = ...) -> None: ...

class CfgTypePricing(_message.Message):
    __slots__ = ["is_buy", "percentile", "modifier", "market"]
    IS_BUY_FIELD_NUMBER: _ClassVar[int]
    PERCENTILE_FIELD_NUMBER: _ClassVar[int]
    MODIFIER_FIELD_NUMBER: _ClassVar[int]
    MARKET_FIELD_NUMBER: _ClassVar[int]
    is_buy: bool
    percentile: int
    modifier: int
    market: str
    def __init__(self, is_buy: bool = ..., percentile: _Optional[int] = ..., modifier: _Optional[int] = ..., market: _Optional[str] = ...) -> None: ...

class CfgBuybackTypePricing(_message.Message):
    __slots__ = ["pricing", "reprocessing_efficiency"]
    PRICING_FIELD_NUMBER: _ClassVar[int]
    REPROCESSING_EFFICIENCY_FIELD_NUMBER: _ClassVar[int]
    pricing: CfgTypePricing
    reprocessing_efficiency: int
    def __init__(self, pricing: _Optional[_Union[CfgTypePricing, _Mapping]] = ..., reprocessing_efficiency: _Optional[int] = ...) -> None: ...

class CfgShopTypePricing(_message.Message):
    __slots__ = ["inner"]
    INNER_FIELD_NUMBER: _ClassVar[int]
    inner: CfgTypePricing
    def __init__(self, inner: _Optional[_Union[CfgTypePricing, _Mapping]] = ...) -> None: ...

class CfgBuybackSystemTypeBundle(_message.Message):
    __slots__ = ["inner"]
    class InnerEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CfgBuybackTypePricing
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CfgBuybackTypePricing, _Mapping]] = ...) -> None: ...
    INNER_FIELD_NUMBER: _ClassVar[int]
    inner: _containers.MessageMap[str, CfgBuybackTypePricing]
    def __init__(self, inner: _Optional[_Mapping[str, CfgBuybackTypePricing]] = ...) -> None: ...

class CfgShopLocationTypeBundle(_message.Message):
    __slots__ = ["inner"]
    class InnerEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CfgShopTypePricing
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CfgShopTypePricing, _Mapping]] = ...) -> None: ...
    INNER_FIELD_NUMBER: _ClassVar[int]
    inner: _containers.MessageMap[str, CfgShopTypePricing]
    def __init__(self, inner: _Optional[_Mapping[str, CfgShopTypePricing]] = ...) -> None: ...

class CfgBuybackSystem(_message.Message):
    __slots__ = ["bundle_key", "m3_fee", "tax_rate"]
    BUNDLE_KEY_FIELD_NUMBER: _ClassVar[int]
    M3_FEE_FIELD_NUMBER: _ClassVar[int]
    TAX_RATE_FIELD_NUMBER: _ClassVar[int]
    bundle_key: str
    m3_fee: float
    tax_rate: float
    def __init__(self, bundle_key: _Optional[str] = ..., m3_fee: _Optional[float] = ..., tax_rate: _Optional[float] = ...) -> None: ...

class CfgShopLocation(_message.Message):
    __slots__ = ["bundle_key", "banned_flags", "tax_rate"]
    BUNDLE_KEY_FIELD_NUMBER: _ClassVar[int]
    BANNED_FLAGS_FIELD_NUMBER: _ClassVar[int]
    TAX_RATE_FIELD_NUMBER: _ClassVar[int]
    bundle_key: str
    banned_flags: _containers.RepeatedScalarFieldContainer[str]
    tax_rate: float
    def __init__(self, bundle_key: _Optional[str] = ..., banned_flags: _Optional[_Iterable[str]] = ..., tax_rate: _Optional[float] = ...) -> None: ...

class CfgMarket(_message.Message):
    __slots__ = ["refresh_token", "location_id", "is_structure"]
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    IS_STRUCTURE_FIELD_NUMBER: _ClassVar[int]
    refresh_token: str
    location_id: int
    is_structure: bool
    def __init__(self, refresh_token: _Optional[str] = ..., location_id: _Optional[int] = ..., is_structure: bool = ...) -> None: ...

class AuthList(_message.Message):
    __slots__ = ["banned_character_ids", "permit_character_ids", "banned_corporation_ids", "permit_corporation_ids", "permit_alliance_ids"]
    BANNED_CHARACTER_IDS_FIELD_NUMBER: _ClassVar[int]
    PERMIT_CHARACTER_IDS_FIELD_NUMBER: _ClassVar[int]
    BANNED_CORPORATION_IDS_FIELD_NUMBER: _ClassVar[int]
    PERMIT_CORPORATION_IDS_FIELD_NUMBER: _ClassVar[int]
    PERMIT_ALLIANCE_IDS_FIELD_NUMBER: _ClassVar[int]
    banned_character_ids: _containers.RepeatedScalarFieldContainer[int]
    permit_character_ids: _containers.RepeatedScalarFieldContainer[int]
    banned_corporation_ids: _containers.RepeatedScalarFieldContainer[int]
    permit_corporation_ids: _containers.RepeatedScalarFieldContainer[int]
    permit_alliance_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, banned_character_ids: _Optional[_Iterable[int]] = ..., permit_character_ids: _Optional[_Iterable[int]] = ..., banned_corporation_ids: _Optional[_Iterable[int]] = ..., permit_corporation_ids: _Optional[_Iterable[int]] = ..., permit_alliance_ids: _Optional[_Iterable[int]] = ...) -> None: ...

class IncludeTypeNaming(_message.Message):
    __slots__ = ["include_name", "include_market_groups", "include_group", "include_category"]
    INCLUDE_NAME_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_MARKET_GROUPS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_GROUP_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    include_name: bool
    include_market_groups: bool
    include_group: bool
    include_category: bool
    def __init__(self, include_name: bool = ..., include_market_groups: bool = ..., include_group: bool = ..., include_category: bool = ...) -> None: ...

class TypeNamingIndexes(_message.Message):
    __slots__ = ["name", "group_index", "category_index", "market_group_indexes"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    GROUP_INDEX_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_INDEX_FIELD_NUMBER: _ClassVar[int]
    MARKET_GROUP_INDEXES_FIELD_NUMBER: _ClassVar[int]
    name: str
    group_index: int
    category_index: int
    market_group_indexes: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, name: _Optional[str] = ..., group_index: _Optional[int] = ..., category_index: _Optional[int] = ..., market_group_indexes: _Optional[_Iterable[int]] = ...) -> None: ...

class TypeNamingLists(_message.Message):
    __slots__ = ["groups", "categories", "market_groups"]
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    MARKET_GROUPS_FIELD_NUMBER: _ClassVar[int]
    groups: _containers.RepeatedScalarFieldContainer[str]
    categories: _containers.RepeatedScalarFieldContainer[str]
    market_groups: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, groups: _Optional[_Iterable[str]] = ..., categories: _Optional[_Iterable[str]] = ..., market_groups: _Optional[_Iterable[str]] = ...) -> None: ...

class LocationInfo(_message.Message):
    __slots__ = ["is_structure", "forbidden_structure", "system_id", "region_id"]
    IS_STRUCTURE_FIELD_NUMBER: _ClassVar[int]
    FORBIDDEN_STRUCTURE_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_ID_FIELD_NUMBER: _ClassVar[int]
    REGION_ID_FIELD_NUMBER: _ClassVar[int]
    is_structure: bool
    forbidden_structure: bool
    system_id: int
    region_id: int
    def __init__(self, is_structure: bool = ..., forbidden_structure: bool = ..., system_id: _Optional[int] = ..., region_id: _Optional[int] = ...) -> None: ...

class IncludeLocationNaming(_message.Message):
    __slots__ = ["include_location_name", "include_system_name", "include_region_name"]
    INCLUDE_LOCATION_NAME_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_SYSTEM_NAME_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_REGION_NAME_FIELD_NUMBER: _ClassVar[int]
    include_location_name: bool
    include_system_name: bool
    include_region_name: bool
    def __init__(self, include_location_name: bool = ..., include_system_name: bool = ..., include_region_name: bool = ...) -> None: ...

class LocationNamingMaps(_message.Message):
    __slots__ = ["location_names", "system_names", "region_names"]
    class LocationNamesEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: str
        def __init__(self, key: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...
    class SystemNamesEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: str
        def __init__(self, key: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...
    class RegionNamesEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: str
        def __init__(self, key: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...
    LOCATION_NAMES_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_NAMES_FIELD_NUMBER: _ClassVar[int]
    REGION_NAMES_FIELD_NUMBER: _ClassVar[int]
    location_names: _containers.ScalarMap[int, str]
    system_names: _containers.ScalarMap[int, str]
    region_names: _containers.ScalarMap[int, str]
    def __init__(self, location_names: _Optional[_Mapping[int, str]] = ..., system_names: _Optional[_Mapping[int, str]] = ..., region_names: _Optional[_Mapping[int, str]] = ...) -> None: ...

class NamedType(_message.Message):
    __slots__ = ["type_id", "type_naming_indexes"]
    TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_NAMING_INDEXES_FIELD_NUMBER: _ClassVar[int]
    type_id: int
    type_naming_indexes: TypeNamingIndexes
    def __init__(self, type_id: _Optional[int] = ..., type_naming_indexes: _Optional[_Union[TypeNamingIndexes, _Mapping]] = ...) -> None: ...

class BasicItem(_message.Message):
    __slots__ = ["type_id", "quantity"]
    TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    type_id: int
    quantity: int
    def __init__(self, type_id: _Optional[int] = ..., quantity: _Optional[int] = ...) -> None: ...

class NamedBasicItem(_message.Message):
    __slots__ = ["type_id", "quantity", "name"]
    TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    type_id: int
    quantity: int
    name: str
    def __init__(self, type_id: _Optional[int] = ..., quantity: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...

class BuybackAppraisal(_message.Message):
    __slots__ = ["items", "code", "price", "time", "version", "system_id", "fee", "fee_per_m3", "tax_rate", "tax"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_ID_FIELD_NUMBER: _ClassVar[int]
    FEE_FIELD_NUMBER: _ClassVar[int]
    FEE_PER_M3_FIELD_NUMBER: _ClassVar[int]
    TAX_RATE_FIELD_NUMBER: _ClassVar[int]
    TAX_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[BuybackParentItem]
    code: str
    price: float
    time: int
    version: str
    system_id: int
    fee: float
    fee_per_m3: float
    tax_rate: float
    tax: float
    def __init__(self, items: _Optional[_Iterable[_Union[BuybackParentItem, _Mapping]]] = ..., code: _Optional[str] = ..., price: _Optional[float] = ..., time: _Optional[int] = ..., version: _Optional[str] = ..., system_id: _Optional[int] = ..., fee: _Optional[float] = ..., fee_per_m3: _Optional[float] = ..., tax_rate: _Optional[float] = ..., tax: _Optional[float] = ...) -> None: ...

class BuybackParentItem(_message.Message):
    __slots__ = ["type_id", "quantity", "price_per_unit", "description", "children", "type_naming_indexes", "fee_per_unit"]
    TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    PRICE_PER_UNIT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CHILDREN_FIELD_NUMBER: _ClassVar[int]
    TYPE_NAMING_INDEXES_FIELD_NUMBER: _ClassVar[int]
    FEE_PER_UNIT_FIELD_NUMBER: _ClassVar[int]
    type_id: int
    quantity: int
    price_per_unit: float
    description: str
    children: _containers.RepeatedCompositeFieldContainer[BuybackChildItem]
    type_naming_indexes: TypeNamingIndexes
    fee_per_unit: float
    def __init__(self, type_id: _Optional[int] = ..., quantity: _Optional[int] = ..., price_per_unit: _Optional[float] = ..., description: _Optional[str] = ..., children: _Optional[_Iterable[_Union[BuybackChildItem, _Mapping]]] = ..., type_naming_indexes: _Optional[_Union[TypeNamingIndexes, _Mapping]] = ..., fee_per_unit: _Optional[float] = ...) -> None: ...

class BuybackChildItem(_message.Message):
    __slots__ = ["type_id", "quantity_per_parent", "price_per_unit", "description", "type_naming_indexes"]
    TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_PER_PARENT_FIELD_NUMBER: _ClassVar[int]
    PRICE_PER_UNIT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TYPE_NAMING_INDEXES_FIELD_NUMBER: _ClassVar[int]
    type_id: int
    quantity_per_parent: float
    price_per_unit: float
    description: str
    type_naming_indexes: TypeNamingIndexes
    def __init__(self, type_id: _Optional[int] = ..., quantity_per_parent: _Optional[float] = ..., price_per_unit: _Optional[float] = ..., description: _Optional[str] = ..., type_naming_indexes: _Optional[_Union[TypeNamingIndexes, _Mapping]] = ...) -> None: ...

class ShopAppraisal(_message.Message):
    __slots__ = ["items", "code", "price", "time", "version", "location_id", "tax_rate", "tax"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    TAX_RATE_FIELD_NUMBER: _ClassVar[int]
    TAX_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[ShopItem]
    code: str
    price: float
    time: int
    version: str
    location_id: int
    tax_rate: float
    tax: float
    def __init__(self, items: _Optional[_Iterable[_Union[ShopItem, _Mapping]]] = ..., code: _Optional[str] = ..., price: _Optional[float] = ..., time: _Optional[int] = ..., version: _Optional[str] = ..., location_id: _Optional[int] = ..., tax_rate: _Optional[float] = ..., tax: _Optional[float] = ...) -> None: ...

class ShopItem(_message.Message):
    __slots__ = ["type_id", "quantity", "price_per_unit", "description", "type_naming_indexes"]
    TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    PRICE_PER_UNIT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TYPE_NAMING_INDEXES_FIELD_NUMBER: _ClassVar[int]
    type_id: int
    quantity: int
    price_per_unit: float
    description: str
    type_naming_indexes: TypeNamingIndexes
    def __init__(self, type_id: _Optional[int] = ..., quantity: _Optional[int] = ..., price_per_unit: _Optional[float] = ..., description: _Optional[str] = ..., type_naming_indexes: _Optional[_Union[TypeNamingIndexes, _Mapping]] = ...) -> None: ...

class ContractItem(_message.Message):
    __slots__ = ["type_id", "quantity", "type_naming_indexes"]
    TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    TYPE_NAMING_INDEXES_FIELD_NUMBER: _ClassVar[int]
    type_id: int
    quantity: int
    type_naming_indexes: TypeNamingIndexes
    def __init__(self, type_id: _Optional[int] = ..., quantity: _Optional[int] = ..., type_naming_indexes: _Optional[_Union[TypeNamingIndexes, _Mapping]] = ...) -> None: ...

class Contract(_message.Message):
    __slots__ = ["contract_id", "status", "issued", "expires", "location_id", "price", "has_reward", "issuer_corp_id", "issuer_char_id", "assignee_id", "assignee_type"]
    CONTRACT_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ISSUED_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_FIELD_NUMBER: _ClassVar[int]
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    HAS_REWARD_FIELD_NUMBER: _ClassVar[int]
    ISSUER_CORP_ID_FIELD_NUMBER: _ClassVar[int]
    ISSUER_CHAR_ID_FIELD_NUMBER: _ClassVar[int]
    ASSIGNEE_ID_FIELD_NUMBER: _ClassVar[int]
    ASSIGNEE_TYPE_FIELD_NUMBER: _ClassVar[int]
    contract_id: int
    status: ContractStatus
    issued: int
    expires: int
    location_id: int
    price: float
    has_reward: bool
    issuer_corp_id: int
    issuer_char_id: int
    assignee_id: int
    assignee_type: ContractAssigneeType
    def __init__(self, contract_id: _Optional[int] = ..., status: _Optional[_Union[ContractStatus, str]] = ..., issued: _Optional[int] = ..., expires: _Optional[int] = ..., location_id: _Optional[int] = ..., price: _Optional[float] = ..., has_reward: bool = ..., issuer_corp_id: _Optional[int] = ..., issuer_char_id: _Optional[int] = ..., assignee_id: _Optional[int] = ..., assignee_type: _Optional[_Union[ContractAssigneeType, str]] = ...) -> None: ...

class ContractQueueEntry(_message.Message):
    __slots__ = ["code", "contract", "contract_location_info", "appraisal_character_id"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_LOCATION_INFO_FIELD_NUMBER: _ClassVar[int]
    APPRAISAL_CHARACTER_ID_FIELD_NUMBER: _ClassVar[int]
    code: str
    contract: Contract
    contract_location_info: LocationInfo
    appraisal_character_id: int
    def __init__(self, code: _Optional[str] = ..., contract: _Optional[_Union[Contract, _Mapping]] = ..., contract_location_info: _Optional[_Union[LocationInfo, _Mapping]] = ..., appraisal_character_id: _Optional[int] = ...) -> None: ...

class PurchaseQueueEntry(_message.Message):
    __slots__ = ["code"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    code: str
    def __init__(self, code: _Optional[str] = ...) -> None: ...

class BuybackAppraisalStatus(_message.Message):
    __slots__ = ["code", "contract"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_FIELD_NUMBER: _ClassVar[int]
    code: str
    contract: Contract
    def __init__(self, code: _Optional[str] = ..., contract: _Optional[_Union[Contract, _Mapping]] = ...) -> None: ...

class ShopAppraisalStatus(_message.Message):
    __slots__ = ["code", "contract", "in_purchase_queue"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_FIELD_NUMBER: _ClassVar[int]
    IN_PURCHASE_QUEUE_FIELD_NUMBER: _ClassVar[int]
    code: str
    contract: Contract
    in_purchase_queue: bool
    def __init__(self, code: _Optional[str] = ..., contract: _Optional[_Union[Contract, _Mapping]] = ..., in_purchase_queue: bool = ...) -> None: ...

class CfgGetAuthListRequest(_message.Message):
    __slots__ = ["domain_key", "auth"]
    DOMAIN_KEY_FIELD_NUMBER: _ClassVar[int]
    AUTH_FIELD_NUMBER: _ClassVar[int]
    domain_key: str
    auth: AuthRequest
    def __init__(self, domain_key: _Optional[str] = ..., auth: _Optional[_Union[AuthRequest, _Mapping]] = ...) -> None: ...

class CfgGetAuthListResponse(_message.Message):
    __slots__ = ["auth_list", "auth", "error"]
    AUTH_LIST_FIELD_NUMBER: _ClassVar[int]
    AUTH_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    auth_list: AuthList
    auth: AuthResponse
    error: ErrorResponse
    def __init__(self, auth_list: _Optional[_Union[AuthList, _Mapping]] = ..., auth: _Optional[_Union[AuthResponse, _Mapping]] = ..., error: _Optional[_Union[ErrorResponse, _Mapping]] = ...) -> None: ...

class CfgSetAuthListRequest(_message.Message):
    __slots__ = ["domain_key", "auth_list", "auth"]
    DOMAIN_KEY_FIELD_NUMBER: _ClassVar[int]
    AUTH_LIST_FIELD_NUMBER: _ClassVar[int]
    AUTH_FIELD_NUMBER: _ClassVar[int]
    domain_key: str
    auth_list: AuthList
    auth: AuthRequest
    def __init__(self, domain_key: _Optional[str] = ..., auth_list: _Optional[_Union[AuthList, _Mapping]] = ..., auth: _Optional[_Union[AuthRequest, _Mapping]] = ...) -> None: ...

class CfgSetAuthListResponse(_message.Message):
    __slots__ = ["auth", "error"]
    AUTH_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    auth: AuthResponse
    error: ErrorResponse
    def __init__(self, auth: _Optional[_Union[AuthResponse, _Mapping]] = ..., error: _Optional[_Union[ErrorResponse, _Mapping]] = ...) -> None: ...

class CfgGetBuybackSystemTypeMapsBuilderRequest(_message.Message):
    __slots__ = ["auth"]
    AUTH_FIELD_NUMBER: _ClassVar[int]
    auth: AuthRequest
    def __init__(self, auth: _Optional[_Union[AuthRequest, _Mapping]] = ...) -> None: ...

class CfgGetBuybackSystemTypeMapsBuilderResponse(_message.Message):
    __slots__ = ["builder", "auth", "error"]
    class BuilderEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: CfgBuybackSystemTypeBundle
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[CfgBuybackSystemTypeBundle, _Mapping]] = ...) -> None: ...
    BUILDER_FIELD_NUMBER: _ClassVar[int]
    AUTH_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    builder: _containers.MessageMap[int, CfgBuybackSystemTypeBundle]
    auth: AuthResponse
    error: ErrorResponse
    def __init__(self, builder: _Optional[_Mapping[int, CfgBuybackSystemTypeBundle]] = ..., auth: _Optional[_Union[AuthResponse, _Mapping]] = ..., error: _Optional[_Union[ErrorResponse, _Mapping]] = ...) -> None: ...

class CfgMergeBuybackSystemTypeMapsBuilderRequest(_message.Message):
    __slots__ = ["builder", "auth"]
    class BuilderEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: CfgBuybackSystemTypeBundle
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[CfgBuybackSystemTypeBundle, _Mapping]] = ...) -> None: ...
    BUILDER_FIELD_NUMBER: _ClassVar[int]
    AUTH_FIELD_NUMBER: _ClassVar[int]
    builder: _containers.MessageMap[int, CfgBuybackSystemTypeBundle]
    auth: AuthRequest
    def __init__(self, builder: _Optional[_Mapping[int, CfgBuybackSystemTypeBundle]] = ..., auth: _Optional[_Union[AuthRequest, _Mapping]] = ...) -> None: ...

class CfgMergeBuybackSystemTypeMapsBuilderResponse(_message.Message):
    __slots__ = ["Modified", "auth", "error"]
    MODIFIED_FIELD_NUMBER: _ClassVar[int]
    AUTH_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    Modified: bool
    auth: AuthResponse
    error: ErrorResponse
    def __init__(self, Modified: bool = ..., auth: _Optional[_Union[AuthResponse, _Mapping]] = ..., error: _Optional[_Union[ErrorResponse, _Mapping]] = ...) -> None: ...

class CfgGetShopLocationTypeMapsBuilderRequest(_message.Message):
    __slots__ = ["auth"]
    AUTH_FIELD_NUMBER: _ClassVar[int]
    auth: AuthRequest
    def __init__(self, auth: _Optional[_Union[AuthRequest, _Mapping]] = ...) -> None: ...

class CfgGetShopLocationTypeMapsBuilderResponse(_message.Message):
    __slots__ = ["builder", "auth", "error"]
    class BuilderEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: CfgShopLocationTypeBundle
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[CfgShopLocationTypeBundle, _Mapping]] = ...) -> None: ...
    BUILDER_FIELD_NUMBER: _ClassVar[int]
    AUTH_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    builder: _containers.MessageMap[int, CfgShopLocationTypeBundle]
    auth: AuthResponse
    error: ErrorResponse
    def __init__(self, builder: _Optional[_Mapping[int, CfgShopLocationTypeBundle]] = ..., auth: _Optional[_Union[AuthResponse, _Mapping]] = ..., error: _Optional[_Union[ErrorResponse, _Mapping]] = ...) -> None: ...

class CfgMergeShopLocationTypeMapsBuilderRequest(_message.Message):
    __slots__ = ["builder", "auth"]
    class BuilderEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: CfgShopLocationTypeBundle
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[CfgShopLocationTypeBundle, _Mapping]] = ...) -> None: ...
    BUILDER_FIELD_NUMBER: _ClassVar[int]
    AUTH_FIELD_NUMBER: _ClassVar[int]
    builder: _containers.MessageMap[int, CfgShopLocationTypeBundle]
    auth: AuthRequest
    def __init__(self, builder: _Optional[_Mapping[int, CfgShopLocationTypeBundle]] = ..., auth: _Optional[_Union[AuthRequest, _Mapping]] = ...) -> None: ...

class CfgMergeShopLocationTypeMapsBuilderResponse(_message.Message):
    __slots__ = ["Modified", "auth", "error"]
    MODIFIED_FIELD_NUMBER: _ClassVar[int]
    AUTH_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    Modified: bool
    auth: AuthResponse
    error: ErrorResponse
    def __init__(self, Modified: bool = ..., auth: _Optional[_Union[AuthResponse, _Mapping]] = ..., error: _Optional[_Union[ErrorResponse, _Mapping]] = ...) -> None: ...

class CfgGetBuybackSystemsRequest(_message.Message):
    __slots__ = ["include_location_info", "include_location_naming", "auth"]
    INCLUDE_LOCATION_INFO_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_LOCATION_NAMING_FIELD_NUMBER: _ClassVar[int]
    AUTH_FIELD_NUMBER: _ClassVar[int]
    include_location_info: bool
    include_location_naming: IncludeLocationNaming
    auth: AuthRequest
    def __init__(self, include_location_info: bool = ..., include_location_naming: _Optional[_Union[IncludeLocationNaming, _Mapping]] = ..., auth: _Optional[_Union[AuthRequest, _Mapping]] = ...) -> None: ...

class CfgGetBuybackSystemsResponse(_message.Message):
    __slots__ = ["systems", "system_region_map", "location_naming_maps", "auth", "error"]
    class SystemsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: CfgBuybackSystem
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[CfgBuybackSystem, _Mapping]] = ...) -> None: ...
    class SystemRegionMapEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    SYSTEMS_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_REGION_MAP_FIELD_NUMBER: _ClassVar[int]
    LOCATION_NAMING_MAPS_FIELD_NUMBER: _ClassVar[int]
    AUTH_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    systems: _containers.MessageMap[int, CfgBuybackSystem]
    system_region_map: _containers.ScalarMap[int, int]
    location_naming_maps: LocationNamingMaps
    auth: AuthResponse
    error: ErrorResponse
    def __init__(self, systems: _Optional[_Mapping[int, CfgBuybackSystem]] = ..., system_region_map: _Optional[_Mapping[int, int]] = ..., location_naming_maps: _Optional[_Union[LocationNamingMaps, _Mapping]] = ..., auth: _Optional[_Union[AuthResponse, _Mapping]] = ..., error: _Optional[_Union[ErrorResponse, _Mapping]] = ...) -> None: ...

class CfgMergeBuybackSystemsRequest(_message.Message):
    __slots__ = ["systems", "auth"]
    class SystemsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: CfgBuybackSystem
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[CfgBuybackSystem, _Mapping]] = ...) -> None: ...
    SYSTEMS_FIELD_NUMBER: _ClassVar[int]
    AUTH_FIELD_NUMBER: _ClassVar[int]
    systems: _containers.MessageMap[int, CfgBuybackSystem]
    auth: AuthRequest
    def __init__(self, systems: _Optional[_Mapping[int, CfgBuybackSystem]] = ..., auth: _Optional[_Union[AuthRequest, _Mapping]] = ...) -> None: ...

class CfgMergeBuybackSystemsResponse(_message.Message):
    __slots__ = ["Modified", "auth", "error"]
    MODIFIED_FIELD_NUMBER: _ClassVar[int]
    AUTH_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    Modified: bool
    auth: AuthResponse
    error: ErrorResponse
    def __init__(self, Modified: bool = ..., auth: _Optional[_Union[AuthResponse, _Mapping]] = ..., error: _Optional[_Union[ErrorResponse, _Mapping]] = ...) -> None: ...

class CfgGetShopLocationsRequest(_message.Message):
    __slots__ = ["include_location_info", "include_location_naming", "auth"]
    INCLUDE_LOCATION_INFO_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_LOCATION_NAMING_FIELD_NUMBER: _ClassVar[int]
    AUTH_FIELD_NUMBER: _ClassVar[int]
    include_location_info: bool
    include_location_naming: IncludeLocationNaming
    auth: AuthRequest
    def __init__(self, include_location_info: bool = ..., include_location_naming: _Optional[_Union[IncludeLocationNaming, _Mapping]] = ..., auth: _Optional[_Union[AuthRequest, _Mapping]] = ...) -> None: ...

class CfgGetShopLocationsResponse(_message.Message):
    __slots__ = ["locations", "location_info_map", "location_naming_maps", "auth", "error"]
    class LocationsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: CfgShopLocation
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[CfgShopLocation, _Mapping]] = ...) -> None: ...
    class LocationInfoMapEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: LocationInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[LocationInfo, _Mapping]] = ...) -> None: ...
    LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    LOCATION_INFO_MAP_FIELD_NUMBER: _ClassVar[int]
    LOCATION_NAMING_MAPS_FIELD_NUMBER: _ClassVar[int]
    AUTH_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    locations: _containers.MessageMap[int, CfgShopLocation]
    location_info_map: _containers.MessageMap[int, LocationInfo]
    location_naming_maps: LocationNamingMaps
    auth: AuthResponse
    error: ErrorResponse
    def __init__(self, locations: _Optional[_Mapping[int, CfgShopLocation]] = ..., location_info_map: _Optional[_Mapping[int, LocationInfo]] = ..., location_naming_maps: _Optional[_Union[LocationNamingMaps, _Mapping]] = ..., auth: _Optional[_Union[AuthResponse, _Mapping]] = ..., error: _Optional[_Union[ErrorResponse, _Mapping]] = ...) -> None: ...

class CfgMergeShopLocationsRequest(_message.Message):
    __slots__ = ["locations", "auth"]
    class LocationsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: CfgShopLocation
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[CfgShopLocation, _Mapping]] = ...) -> None: ...
    LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    AUTH_FIELD_NUMBER: _ClassVar[int]
    locations: _containers.MessageMap[int, CfgShopLocation]
    auth: AuthRequest
    def __init__(self, locations: _Optional[_Mapping[int, CfgShopLocation]] = ..., auth: _Optional[_Union[AuthRequest, _Mapping]] = ...) -> None: ...

class CfgMergeShopLocationsResponse(_message.Message):
    __slots__ = ["Modified", "auth", "error"]
    MODIFIED_FIELD_NUMBER: _ClassVar[int]
    AUTH_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    Modified: bool
    auth: AuthResponse
    error: ErrorResponse
    def __init__(self, Modified: bool = ..., auth: _Optional[_Union[AuthResponse, _Mapping]] = ..., error: _Optional[_Union[ErrorResponse, _Mapping]] = ...) -> None: ...

class CfgGetMarketsRequest(_message.Message):
    __slots__ = ["include_location_info", "include_location_naming", "auth"]
    INCLUDE_LOCATION_INFO_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_LOCATION_NAMING_FIELD_NUMBER: _ClassVar[int]
    AUTH_FIELD_NUMBER: _ClassVar[int]
    include_location_info: bool
    include_location_naming: IncludeLocationNaming
    auth: AuthRequest
    def __init__(self, include_location_info: bool = ..., include_location_naming: _Optional[_Union[IncludeLocationNaming, _Mapping]] = ..., auth: _Optional[_Union[AuthRequest, _Mapping]] = ...) -> None: ...

class CfgGetMarketsResponse(_message.Message):
    __slots__ = ["markets", "location_info_map", "location_naming_maps", "auth", "error"]
    class MarketsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CfgMarket
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CfgMarket, _Mapping]] = ...) -> None: ...
    class LocationInfoMapEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: LocationInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[LocationInfo, _Mapping]] = ...) -> None: ...
    MARKETS_FIELD_NUMBER: _ClassVar[int]
    LOCATION_INFO_MAP_FIELD_NUMBER: _ClassVar[int]
    LOCATION_NAMING_MAPS_FIELD_NUMBER: _ClassVar[int]
    AUTH_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    markets: _containers.MessageMap[str, CfgMarket]
    location_info_map: _containers.MessageMap[int, LocationInfo]
    location_naming_maps: LocationNamingMaps
    auth: AuthResponse
    error: ErrorResponse
    def __init__(self, markets: _Optional[_Mapping[str, CfgMarket]] = ..., location_info_map: _Optional[_Mapping[int, LocationInfo]] = ..., location_naming_maps: _Optional[_Union[LocationNamingMaps, _Mapping]] = ..., auth: _Optional[_Union[AuthResponse, _Mapping]] = ..., error: _Optional[_Union[ErrorResponse, _Mapping]] = ...) -> None: ...

class CfgMergeMarketsRequest(_message.Message):
    __slots__ = ["markets", "auth"]
    class MarketsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CfgMarket
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CfgMarket, _Mapping]] = ...) -> None: ...
    MARKETS_FIELD_NUMBER: _ClassVar[int]
    AUTH_FIELD_NUMBER: _ClassVar[int]
    markets: _containers.MessageMap[str, CfgMarket]
    auth: AuthRequest
    def __init__(self, markets: _Optional[_Mapping[str, CfgMarket]] = ..., auth: _Optional[_Union[AuthRequest, _Mapping]] = ...) -> None: ...

class CfgMergeMarketsResponse(_message.Message):
    __slots__ = ["Modified", "auth", "error"]
    MODIFIED_FIELD_NUMBER: _ClassVar[int]
    AUTH_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    Modified: bool
    auth: AuthResponse
    error: ErrorResponse
    def __init__(self, Modified: bool = ..., auth: _Optional[_Union[AuthResponse, _Mapping]] = ..., error: _Optional[_Union[ErrorResponse, _Mapping]] = ...) -> None: ...

class NewBuybackAppraisalRequest(_message.Message):
    __slots__ = ["system_id", "items", "save", "include_type_naming", "auth"]
    SYSTEM_ID_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    SAVE_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_TYPE_NAMING_FIELD_NUMBER: _ClassVar[int]
    AUTH_FIELD_NUMBER: _ClassVar[int]
    system_id: int
    items: _containers.RepeatedCompositeFieldContainer[BasicItem]
    save: bool
    include_type_naming: IncludeTypeNaming
    auth: AuthRequest
    def __init__(self, system_id: _Optional[int] = ..., items: _Optional[_Iterable[_Union[BasicItem, _Mapping]]] = ..., save: bool = ..., include_type_naming: _Optional[_Union[IncludeTypeNaming, _Mapping]] = ..., auth: _Optional[_Union[AuthRequest, _Mapping]] = ...) -> None: ...

class NewBuybackAppraisalResponse(_message.Message):
    __slots__ = ["appraisal", "type_naming_lists", "auth", "error"]
    APPRAISAL_FIELD_NUMBER: _ClassVar[int]
    TYPE_NAMING_LISTS_FIELD_NUMBER: _ClassVar[int]
    AUTH_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    appraisal: BuybackAppraisal
    type_naming_lists: TypeNamingLists
    auth: AuthResponse
    error: ErrorResponse
    def __init__(self, appraisal: _Optional[_Union[BuybackAppraisal, _Mapping]] = ..., type_naming_lists: _Optional[_Union[TypeNamingLists, _Mapping]] = ..., auth: _Optional[_Union[AuthResponse, _Mapping]] = ..., error: _Optional[_Union[ErrorResponse, _Mapping]] = ...) -> None: ...

class NewShopAppraisalRequest(_message.Message):
    __slots__ = ["location_id", "items", "include_type_naming"]
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_TYPE_NAMING_FIELD_NUMBER: _ClassVar[int]
    location_id: int
    items: _containers.RepeatedCompositeFieldContainer[BasicItem]
    include_type_naming: IncludeTypeNaming
    def __init__(self, location_id: _Optional[int] = ..., items: _Optional[_Iterable[_Union[BasicItem, _Mapping]]] = ..., include_type_naming: _Optional[_Union[IncludeTypeNaming, _Mapping]] = ...) -> None: ...

class NewShopAppraisalResponse(_message.Message):
    __slots__ = ["appraisal", "type_naming_lists", "error"]
    APPRAISAL_FIELD_NUMBER: _ClassVar[int]
    TYPE_NAMING_LISTS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    appraisal: ShopAppraisal
    type_naming_lists: TypeNamingLists
    error: ErrorResponse
    def __init__(self, appraisal: _Optional[_Union[ShopAppraisal, _Mapping]] = ..., type_naming_lists: _Optional[_Union[TypeNamingLists, _Mapping]] = ..., error: _Optional[_Union[ErrorResponse, _Mapping]] = ...) -> None: ...

class GetBuybackAppraisalRequest(_message.Message):
    __slots__ = ["code", "include_type_naming", "admin", "auth"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_TYPE_NAMING_FIELD_NUMBER: _ClassVar[int]
    ADMIN_FIELD_NUMBER: _ClassVar[int]
    AUTH_FIELD_NUMBER: _ClassVar[int]
    code: str
    include_type_naming: IncludeTypeNaming
    admin: bool
    auth: AuthRequest
    def __init__(self, code: _Optional[str] = ..., include_type_naming: _Optional[_Union[IncludeTypeNaming, _Mapping]] = ..., admin: bool = ..., auth: _Optional[_Union[AuthRequest, _Mapping]] = ...) -> None: ...

class GetBuybackAppraisalResponse(_message.Message):
    __slots__ = ["appraisal", "hash_character_id", "character_id", "type_naming_lists", "auth", "error"]
    APPRAISAL_FIELD_NUMBER: _ClassVar[int]
    HASH_CHARACTER_ID_FIELD_NUMBER: _ClassVar[int]
    CHARACTER_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_NAMING_LISTS_FIELD_NUMBER: _ClassVar[int]
    AUTH_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    appraisal: BuybackAppraisal
    hash_character_id: str
    character_id: int
    type_naming_lists: TypeNamingLists
    auth: AuthResponse
    error: ErrorResponse
    def __init__(self, appraisal: _Optional[_Union[BuybackAppraisal, _Mapping]] = ..., hash_character_id: _Optional[str] = ..., character_id: _Optional[int] = ..., type_naming_lists: _Optional[_Union[TypeNamingLists, _Mapping]] = ..., auth: _Optional[_Union[AuthResponse, _Mapping]] = ..., error: _Optional[_Union[ErrorResponse, _Mapping]] = ...) -> None: ...

class GetShopAppraisalRequest(_message.Message):
    __slots__ = ["code", "include_type_naming", "admin", "auth"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_TYPE_NAMING_FIELD_NUMBER: _ClassVar[int]
    ADMIN_FIELD_NUMBER: _ClassVar[int]
    AUTH_FIELD_NUMBER: _ClassVar[int]
    code: str
    include_type_naming: IncludeTypeNaming
    admin: bool
    auth: AuthRequest
    def __init__(self, code: _Optional[str] = ..., include_type_naming: _Optional[_Union[IncludeTypeNaming, _Mapping]] = ..., admin: bool = ..., auth: _Optional[_Union[AuthRequest, _Mapping]] = ...) -> None: ...

class GetShopAppraisalResponse(_message.Message):
    __slots__ = ["appraisal", "hash_character_id", "character_id", "type_naming_lists", "auth", "error"]
    APPRAISAL_FIELD_NUMBER: _ClassVar[int]
    HASH_CHARACTER_ID_FIELD_NUMBER: _ClassVar[int]
    CHARACTER_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_NAMING_LISTS_FIELD_NUMBER: _ClassVar[int]
    AUTH_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    appraisal: ShopAppraisal
    hash_character_id: str
    character_id: int
    type_naming_lists: TypeNamingLists
    auth: AuthResponse
    error: ErrorResponse
    def __init__(self, appraisal: _Optional[_Union[ShopAppraisal, _Mapping]] = ..., hash_character_id: _Optional[str] = ..., character_id: _Optional[int] = ..., type_naming_lists: _Optional[_Union[TypeNamingLists, _Mapping]] = ..., auth: _Optional[_Union[AuthResponse, _Mapping]] = ..., error: _Optional[_Union[ErrorResponse, _Mapping]] = ...) -> None: ...

class StatusBuybackAppraisalRequest(_message.Message):
    __slots__ = ["code", "include_items", "include_location_info", "include_type_naming", "include_location_naming", "admin", "auth"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_ITEMS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_LOCATION_INFO_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_TYPE_NAMING_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_LOCATION_NAMING_FIELD_NUMBER: _ClassVar[int]
    ADMIN_FIELD_NUMBER: _ClassVar[int]
    AUTH_FIELD_NUMBER: _ClassVar[int]
    code: str
    include_items: bool
    include_location_info: bool
    include_type_naming: IncludeTypeNaming
    include_location_naming: IncludeLocationNaming
    admin: bool
    auth: AuthRequest
    def __init__(self, code: _Optional[str] = ..., include_items: bool = ..., include_location_info: bool = ..., include_type_naming: _Optional[_Union[IncludeTypeNaming, _Mapping]] = ..., include_location_naming: _Optional[_Union[IncludeLocationNaming, _Mapping]] = ..., admin: bool = ..., auth: _Optional[_Union[AuthRequest, _Mapping]] = ...) -> None: ...

class StatusBuybackAppraisalResponse(_message.Message):
    __slots__ = ["contract", "contract_items", "location_info", "type_naming_lists", "location_naming_maps", "auth", "error"]
    CONTRACT_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_ITEMS_FIELD_NUMBER: _ClassVar[int]
    LOCATION_INFO_FIELD_NUMBER: _ClassVar[int]
    TYPE_NAMING_LISTS_FIELD_NUMBER: _ClassVar[int]
    LOCATION_NAMING_MAPS_FIELD_NUMBER: _ClassVar[int]
    AUTH_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    contract: Contract
    contract_items: _containers.RepeatedCompositeFieldContainer[ContractItem]
    location_info: LocationInfo
    type_naming_lists: TypeNamingLists
    location_naming_maps: LocationNamingMaps
    auth: AuthResponse
    error: ErrorResponse
    def __init__(self, contract: _Optional[_Union[Contract, _Mapping]] = ..., contract_items: _Optional[_Iterable[_Union[ContractItem, _Mapping]]] = ..., location_info: _Optional[_Union[LocationInfo, _Mapping]] = ..., type_naming_lists: _Optional[_Union[TypeNamingLists, _Mapping]] = ..., location_naming_maps: _Optional[_Union[LocationNamingMaps, _Mapping]] = ..., auth: _Optional[_Union[AuthResponse, _Mapping]] = ..., error: _Optional[_Union[ErrorResponse, _Mapping]] = ...) -> None: ...

class StatusShopAppraisalRequest(_message.Message):
    __slots__ = ["code", "include_items", "include_location_info", "include_type_naming", "include_location_naming", "admin", "auth"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_ITEMS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_LOCATION_INFO_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_TYPE_NAMING_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_LOCATION_NAMING_FIELD_NUMBER: _ClassVar[int]
    ADMIN_FIELD_NUMBER: _ClassVar[int]
    AUTH_FIELD_NUMBER: _ClassVar[int]
    code: str
    include_items: bool
    include_location_info: bool
    include_type_naming: IncludeTypeNaming
    include_location_naming: IncludeLocationNaming
    admin: bool
    auth: AuthRequest
    def __init__(self, code: _Optional[str] = ..., include_items: bool = ..., include_location_info: bool = ..., include_type_naming: _Optional[_Union[IncludeTypeNaming, _Mapping]] = ..., include_location_naming: _Optional[_Union[IncludeLocationNaming, _Mapping]] = ..., admin: bool = ..., auth: _Optional[_Union[AuthRequest, _Mapping]] = ...) -> None: ...

class StatusShopAppraisalResponse(_message.Message):
    __slots__ = ["contract", "in_purchase_queue", "contract_items", "location_info", "type_naming_lists", "location_naming_maps", "auth", "error"]
    CONTRACT_FIELD_NUMBER: _ClassVar[int]
    IN_PURCHASE_QUEUE_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_ITEMS_FIELD_NUMBER: _ClassVar[int]
    LOCATION_INFO_FIELD_NUMBER: _ClassVar[int]
    TYPE_NAMING_LISTS_FIELD_NUMBER: _ClassVar[int]
    LOCATION_NAMING_MAPS_FIELD_NUMBER: _ClassVar[int]
    AUTH_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    contract: Contract
    in_purchase_queue: bool
    contract_items: _containers.RepeatedCompositeFieldContainer[ContractItem]
    location_info: LocationInfo
    type_naming_lists: TypeNamingLists
    location_naming_maps: LocationNamingMaps
    auth: AuthResponse
    error: ErrorResponse
    def __init__(self, contract: _Optional[_Union[Contract, _Mapping]] = ..., in_purchase_queue: bool = ..., contract_items: _Optional[_Iterable[_Union[ContractItem, _Mapping]]] = ..., location_info: _Optional[_Union[LocationInfo, _Mapping]] = ..., type_naming_lists: _Optional[_Union[TypeNamingLists, _Mapping]] = ..., location_naming_maps: _Optional[_Union[LocationNamingMaps, _Mapping]] = ..., auth: _Optional[_Union[AuthResponse, _Mapping]] = ..., error: _Optional[_Union[ErrorResponse, _Mapping]] = ...) -> None: ...

class ShopInventoryRequest(_message.Message):
    __slots__ = ["location_id", "include_type_naming", "auth"]
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_TYPE_NAMING_FIELD_NUMBER: _ClassVar[int]
    AUTH_FIELD_NUMBER: _ClassVar[int]
    location_id: int
    include_type_naming: IncludeTypeNaming
    auth: AuthRequest
    def __init__(self, location_id: _Optional[int] = ..., include_type_naming: _Optional[_Union[IncludeTypeNaming, _Mapping]] = ..., auth: _Optional[_Union[AuthRequest, _Mapping]] = ...) -> None: ...

class ShopInventoryResponse(_message.Message):
    __slots__ = ["items", "type_naming_lists", "auth", "error"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TYPE_NAMING_LISTS_FIELD_NUMBER: _ClassVar[int]
    AUTH_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[ShopItem]
    type_naming_lists: TypeNamingLists
    auth: AuthResponse
    error: ErrorResponse
    def __init__(self, items: _Optional[_Iterable[_Union[ShopItem, _Mapping]]] = ..., type_naming_lists: _Optional[_Union[TypeNamingLists, _Mapping]] = ..., auth: _Optional[_Union[AuthResponse, _Mapping]] = ..., error: _Optional[_Union[ErrorResponse, _Mapping]] = ...) -> None: ...

class ShopMakePurchaseRequest(_message.Message):
    __slots__ = ["location_id", "items", "include_type_naming", "auth"]
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_TYPE_NAMING_FIELD_NUMBER: _ClassVar[int]
    AUTH_FIELD_NUMBER: _ClassVar[int]
    location_id: int
    items: _containers.RepeatedCompositeFieldContainer[BasicItem]
    include_type_naming: IncludeTypeNaming
    auth: AuthRequest
    def __init__(self, location_id: _Optional[int] = ..., items: _Optional[_Iterable[_Union[BasicItem, _Mapping]]] = ..., include_type_naming: _Optional[_Union[IncludeTypeNaming, _Mapping]] = ..., auth: _Optional[_Union[AuthRequest, _Mapping]] = ...) -> None: ...

class ShopMakePurchaseResponse(_message.Message):
    __slots__ = ["status", "appraisal", "type_naming_lists", "auth", "error"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    APPRAISAL_FIELD_NUMBER: _ClassVar[int]
    TYPE_NAMING_LISTS_FIELD_NUMBER: _ClassVar[int]
    AUTH_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    status: MakePurchaseStatus
    appraisal: ShopAppraisal
    type_naming_lists: TypeNamingLists
    auth: AuthResponse
    error: ErrorResponse
    def __init__(self, status: _Optional[_Union[MakePurchaseStatus, str]] = ..., appraisal: _Optional[_Union[ShopAppraisal, _Mapping]] = ..., type_naming_lists: _Optional[_Union[TypeNamingLists, _Mapping]] = ..., auth: _Optional[_Union[AuthResponse, _Mapping]] = ..., error: _Optional[_Union[ErrorResponse, _Mapping]] = ...) -> None: ...

class UserDataRequest(_message.Message):
    __slots__ = ["auth"]
    AUTH_FIELD_NUMBER: _ClassVar[int]
    auth: AuthRequest
    def __init__(self, auth: _Optional[_Union[AuthRequest, _Mapping]] = ...) -> None: ...

class UserDataResponse(_message.Message):
    __slots__ = ["buyback_appraisals", "shop_appraisals", "cancelled_purchase", "made_purchase", "auth", "error"]
    BUYBACK_APPRAISALS_FIELD_NUMBER: _ClassVar[int]
    SHOP_APPRAISALS_FIELD_NUMBER: _ClassVar[int]
    CANCELLED_PURCHASE_FIELD_NUMBER: _ClassVar[int]
    MADE_PURCHASE_FIELD_NUMBER: _ClassVar[int]
    AUTH_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    buyback_appraisals: _containers.RepeatedCompositeFieldContainer[BuybackAppraisalStatus]
    shop_appraisals: _containers.RepeatedCompositeFieldContainer[ShopAppraisalStatus]
    cancelled_purchase: int
    made_purchase: int
    auth: AuthResponse
    error: ErrorResponse
    def __init__(self, buyback_appraisals: _Optional[_Iterable[_Union[BuybackAppraisalStatus, _Mapping]]] = ..., shop_appraisals: _Optional[_Iterable[_Union[ShopAppraisalStatus, _Mapping]]] = ..., cancelled_purchase: _Optional[int] = ..., made_purchase: _Optional[int] = ..., auth: _Optional[_Union[AuthResponse, _Mapping]] = ..., error: _Optional[_Union[ErrorResponse, _Mapping]] = ...) -> None: ...

class ShopContractQueueRequest(_message.Message):
    __slots__ = ["include_location_info", "include_location_naming", "auth"]
    INCLUDE_LOCATION_INFO_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_LOCATION_NAMING_FIELD_NUMBER: _ClassVar[int]
    AUTH_FIELD_NUMBER: _ClassVar[int]
    include_location_info: bool
    include_location_naming: IncludeLocationNaming
    auth: AuthRequest
    def __init__(self, include_location_info: bool = ..., include_location_naming: _Optional[_Union[IncludeLocationNaming, _Mapping]] = ..., auth: _Optional[_Union[AuthRequest, _Mapping]] = ...) -> None: ...

class ShopContractQueueResponse(_message.Message):
    __slots__ = ["queue", "location_naming_maps", "auth", "error"]
    QUEUE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_NAMING_MAPS_FIELD_NUMBER: _ClassVar[int]
    AUTH_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    queue: _containers.RepeatedCompositeFieldContainer[ContractQueueEntry]
    location_naming_maps: LocationNamingMaps
    auth: AuthResponse
    error: ErrorResponse
    def __init__(self, queue: _Optional[_Iterable[_Union[ContractQueueEntry, _Mapping]]] = ..., location_naming_maps: _Optional[_Union[LocationNamingMaps, _Mapping]] = ..., auth: _Optional[_Union[AuthResponse, _Mapping]] = ..., error: _Optional[_Union[ErrorResponse, _Mapping]] = ...) -> None: ...

class BuybackContractQueueRequest(_message.Message):
    __slots__ = ["include_location_info", "include_location_naming", "auth"]
    INCLUDE_LOCATION_INFO_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_LOCATION_NAMING_FIELD_NUMBER: _ClassVar[int]
    AUTH_FIELD_NUMBER: _ClassVar[int]
    include_location_info: bool
    include_location_naming: IncludeLocationNaming
    auth: AuthRequest
    def __init__(self, include_location_info: bool = ..., include_location_naming: _Optional[_Union[IncludeLocationNaming, _Mapping]] = ..., auth: _Optional[_Union[AuthRequest, _Mapping]] = ...) -> None: ...

class BuybackContractQueueResponse(_message.Message):
    __slots__ = ["queue", "location_naming_maps", "auth", "error"]
    QUEUE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_NAMING_MAPS_FIELD_NUMBER: _ClassVar[int]
    AUTH_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    queue: _containers.RepeatedCompositeFieldContainer[ContractQueueEntry]
    location_naming_maps: LocationNamingMaps
    auth: AuthResponse
    error: ErrorResponse
    def __init__(self, queue: _Optional[_Iterable[_Union[ContractQueueEntry, _Mapping]]] = ..., location_naming_maps: _Optional[_Union[LocationNamingMaps, _Mapping]] = ..., auth: _Optional[_Union[AuthResponse, _Mapping]] = ..., error: _Optional[_Union[ErrorResponse, _Mapping]] = ...) -> None: ...

class ShopCancelPurchaseRequest(_message.Message):
    __slots__ = ["code", "auth"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    AUTH_FIELD_NUMBER: _ClassVar[int]
    code: str
    auth: AuthRequest
    def __init__(self, code: _Optional[str] = ..., auth: _Optional[_Union[AuthRequest, _Mapping]] = ...) -> None: ...

class ShopCancelPurchaseResponse(_message.Message):
    __slots__ = ["status", "auth", "error"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    AUTH_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    status: CancelPurchaseStatus
    auth: AuthResponse
    error: ErrorResponse
    def __init__(self, status: _Optional[_Union[CancelPurchaseStatus, str]] = ..., auth: _Optional[_Union[AuthResponse, _Mapping]] = ..., error: _Optional[_Union[ErrorResponse, _Mapping]] = ...) -> None: ...

class ShopDeletePurchasesRequest(_message.Message):
    __slots__ = ["codes", "auth"]
    CODES_FIELD_NUMBER: _ClassVar[int]
    AUTH_FIELD_NUMBER: _ClassVar[int]
    codes: _containers.RepeatedScalarFieldContainer[str]
    auth: AuthRequest
    def __init__(self, codes: _Optional[_Iterable[str]] = ..., auth: _Optional[_Union[AuthRequest, _Mapping]] = ...) -> None: ...

class ShopDeletePurchasesResponse(_message.Message):
    __slots__ = ["auth", "error"]
    AUTH_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    auth: AuthResponse
    error: ErrorResponse
    def __init__(self, auth: _Optional[_Union[AuthResponse, _Mapping]] = ..., error: _Optional[_Union[ErrorResponse, _Mapping]] = ...) -> None: ...

class ParseRequest(_message.Message):
    __slots__ = ["text"]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    text: str
    def __init__(self, text: _Optional[str] = ...) -> None: ...

class ParseResponse(_message.Message):
    __slots__ = ["known_items", "unknown_items", "error"]
    KNOWN_ITEMS_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_ITEMS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    known_items: _containers.RepeatedCompositeFieldContainer[NamedBasicItem]
    unknown_items: _containers.RepeatedCompositeFieldContainer[NamedBasicItem]
    error: ErrorResponse
    def __init__(self, known_items: _Optional[_Iterable[_Union[NamedBasicItem, _Mapping]]] = ..., unknown_items: _Optional[_Iterable[_Union[NamedBasicItem, _Mapping]]] = ..., error: _Optional[_Union[ErrorResponse, _Mapping]] = ...) -> None: ...

class SDETypeDataRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SDETypeDataResponse(_message.Message):
    __slots__ = ["types", "error"]
    TYPES_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    types: _containers.RepeatedScalarFieldContainer[int]
    error: ErrorResponse
    def __init__(self, types: _Optional[_Iterable[int]] = ..., error: _Optional[_Union[ErrorResponse, _Mapping]] = ...) -> None: ...

class NamedSDETypeDataRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class NamedSDETypeDataResponse(_message.Message):
    __slots__ = ["types", "type_naming_lists", "error"]
    TYPES_FIELD_NUMBER: _ClassVar[int]
    TYPE_NAMING_LISTS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    types: _containers.RepeatedCompositeFieldContainer[NamedType]
    type_naming_lists: TypeNamingLists
    error: ErrorResponse
    def __init__(self, types: _Optional[_Iterable[_Union[NamedType, _Mapping]]] = ..., type_naming_lists: _Optional[_Union[TypeNamingLists, _Mapping]] = ..., error: _Optional[_Union[ErrorResponse, _Mapping]] = ...) -> None: ...

class ShopLocation(_message.Message):
    __slots__ = ["location_id", "location_info"]
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    LOCATION_INFO_FIELD_NUMBER: _ClassVar[int]
    location_id: int
    location_info: LocationInfo
    def __init__(self, location_id: _Optional[int] = ..., location_info: _Optional[_Union[LocationInfo, _Mapping]] = ...) -> None: ...

class ShopLocationsRequest(_message.Message):
    __slots__ = ["include_location_info", "include_location_naming"]
    INCLUDE_LOCATION_INFO_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_LOCATION_NAMING_FIELD_NUMBER: _ClassVar[int]
    include_location_info: bool
    include_location_naming: IncludeLocationNaming
    def __init__(self, include_location_info: bool = ..., include_location_naming: _Optional[_Union[IncludeLocationNaming, _Mapping]] = ...) -> None: ...

class ShopLocationsResponse(_message.Message):
    __slots__ = ["locations", "location_naming_maps", "error"]
    LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    LOCATION_NAMING_MAPS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    locations: _containers.RepeatedCompositeFieldContainer[ShopLocation]
    location_naming_maps: LocationNamingMaps
    error: ErrorResponse
    def __init__(self, locations: _Optional[_Iterable[_Union[ShopLocation, _Mapping]]] = ..., location_naming_maps: _Optional[_Union[LocationNamingMaps, _Mapping]] = ..., error: _Optional[_Union[ErrorResponse, _Mapping]] = ...) -> None: ...

class System(_message.Message):
    __slots__ = ["system_id", "region_id"]
    SYSTEM_ID_FIELD_NUMBER: _ClassVar[int]
    REGION_ID_FIELD_NUMBER: _ClassVar[int]
    system_id: int
    region_id: int
    def __init__(self, system_id: _Optional[int] = ..., region_id: _Optional[int] = ...) -> None: ...

class BuybackSystemsRequest(_message.Message):
    __slots__ = ["include_location_naming"]
    INCLUDE_LOCATION_NAMING_FIELD_NUMBER: _ClassVar[int]
    include_location_naming: IncludeLocationNaming
    def __init__(self, include_location_naming: _Optional[_Union[IncludeLocationNaming, _Mapping]] = ...) -> None: ...

class BuybackSystemsResponse(_message.Message):
    __slots__ = ["systems", "location_naming_maps", "error"]
    SYSTEMS_FIELD_NUMBER: _ClassVar[int]
    LOCATION_NAMING_MAPS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    systems: _containers.RepeatedCompositeFieldContainer[System]
    location_naming_maps: LocationNamingMaps
    error: ErrorResponse
    def __init__(self, systems: _Optional[_Iterable[_Union[System, _Mapping]]] = ..., location_naming_maps: _Optional[_Union[LocationNamingMaps, _Mapping]] = ..., error: _Optional[_Union[ErrorResponse, _Mapping]] = ...) -> None: ...

class ShopPurchaseQueueRequest(_message.Message):
    __slots__ = ["auth"]
    AUTH_FIELD_NUMBER: _ClassVar[int]
    auth: AuthRequest
    def __init__(self, auth: _Optional[_Union[AuthRequest, _Mapping]] = ...) -> None: ...

class ShopPurchaseQueueResponse(_message.Message):
    __slots__ = ["queue", "auth", "error"]
    QUEUE_FIELD_NUMBER: _ClassVar[int]
    AUTH_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    queue: _containers.RepeatedCompositeFieldContainer[PurchaseQueueEntry]
    auth: AuthResponse
    error: ErrorResponse
    def __init__(self, queue: _Optional[_Iterable[_Union[PurchaseQueueEntry, _Mapping]]] = ..., auth: _Optional[_Union[AuthResponse, _Mapping]] = ..., error: _Optional[_Union[ErrorResponse, _Mapping]] = ...) -> None: ...

class EsiAppLoginRequest(_message.Message):
    __slots__ = ["code", "app", "auth"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    APP_FIELD_NUMBER: _ClassVar[int]
    AUTH_FIELD_NUMBER: _ClassVar[int]
    code: str
    app: EsiApp
    auth: AuthRequest
    def __init__(self, code: _Optional[str] = ..., app: _Optional[_Union[EsiApp, str]] = ..., auth: _Optional[_Union[AuthRequest, _Mapping]] = ...) -> None: ...

class EsiAppLoginResponse(_message.Message):
    __slots__ = ["token", "jwt", "auth", "error"]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    JWT_FIELD_NUMBER: _ClassVar[int]
    AUTH_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    token: str
    jwt: str
    auth: AuthResponse
    error: ErrorResponse
    def __init__(self, token: _Optional[str] = ..., jwt: _Optional[str] = ..., auth: _Optional[_Union[AuthResponse, _Mapping]] = ..., error: _Optional[_Union[ErrorResponse, _Mapping]] = ...) -> None: ...

class SDESystem(_message.Message):
    __slots__ = ["system_id", "region_id"]
    SYSTEM_ID_FIELD_NUMBER: _ClassVar[int]
    REGION_ID_FIELD_NUMBER: _ClassVar[int]
    system_id: int
    region_id: int
    def __init__(self, system_id: _Optional[int] = ..., region_id: _Optional[int] = ...) -> None: ...

class SDESystemsRequest(_message.Message):
    __slots__ = ["include_location_naming"]
    INCLUDE_LOCATION_NAMING_FIELD_NUMBER: _ClassVar[int]
    include_location_naming: IncludeLocationNaming
    def __init__(self, include_location_naming: _Optional[_Union[IncludeLocationNaming, _Mapping]] = ...) -> None: ...

class SDESystemsResponse(_message.Message):
    __slots__ = ["systems", "location_naming_maps", "error"]
    SYSTEMS_FIELD_NUMBER: _ClassVar[int]
    LOCATION_NAMING_MAPS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    systems: _containers.RepeatedCompositeFieldContainer[System]
    location_naming_maps: LocationNamingMaps
    error: ErrorResponse
    def __init__(self, systems: _Optional[_Iterable[_Union[System, _Mapping]]] = ..., location_naming_maps: _Optional[_Union[LocationNamingMaps, _Mapping]] = ..., error: _Optional[_Union[ErrorResponse, _Mapping]] = ...) -> None: ...

class CfgGetBuybackBundleKeysRequest(_message.Message):
    __slots__ = ["auth"]
    AUTH_FIELD_NUMBER: _ClassVar[int]
    auth: AuthRequest
    def __init__(self, auth: _Optional[_Union[AuthRequest, _Mapping]] = ...) -> None: ...

class CfgGetBuybackBundleKeysResponse(_message.Message):
    __slots__ = ["bundle_keys", "auth", "error"]
    BUNDLE_KEYS_FIELD_NUMBER: _ClassVar[int]
    AUTH_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    bundle_keys: _containers.RepeatedScalarFieldContainer[str]
    auth: AuthResponse
    error: ErrorResponse
    def __init__(self, bundle_keys: _Optional[_Iterable[str]] = ..., auth: _Optional[_Union[AuthResponse, _Mapping]] = ..., error: _Optional[_Union[ErrorResponse, _Mapping]] = ...) -> None: ...

class CfgGetShopBundleKeysRequest(_message.Message):
    __slots__ = ["auth"]
    AUTH_FIELD_NUMBER: _ClassVar[int]
    auth: AuthRequest
    def __init__(self, auth: _Optional[_Union[AuthRequest, _Mapping]] = ...) -> None: ...

class CfgGetShopBundleKeysResponse(_message.Message):
    __slots__ = ["bundle_keys", "auth", "error"]
    BUNDLE_KEYS_FIELD_NUMBER: _ClassVar[int]
    AUTH_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    bundle_keys: _containers.RepeatedScalarFieldContainer[str]
    auth: AuthResponse
    error: ErrorResponse
    def __init__(self, bundle_keys: _Optional[_Iterable[str]] = ..., auth: _Optional[_Union[AuthResponse, _Mapping]] = ..., error: _Optional[_Union[ErrorResponse, _Mapping]] = ...) -> None: ...

class CfgGetMarketNamesRequest(_message.Message):
    __slots__ = ["auth"]
    AUTH_FIELD_NUMBER: _ClassVar[int]
    auth: AuthRequest
    def __init__(self, auth: _Optional[_Union[AuthRequest, _Mapping]] = ...) -> None: ...

class CfgGetMarketNamesResponse(_message.Message):
    __slots__ = ["market_names", "auth", "error"]
    MARKET_NAMES_FIELD_NUMBER: _ClassVar[int]
    AUTH_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    market_names: _containers.RepeatedScalarFieldContainer[str]
    auth: AuthResponse
    error: ErrorResponse
    def __init__(self, market_names: _Optional[_Iterable[str]] = ..., auth: _Optional[_Union[AuthResponse, _Mapping]] = ..., error: _Optional[_Union[ErrorResponse, _Mapping]] = ...) -> None: ...

class ConstData(_message.Message):
    __slots__ = ["purchase_max_active", "make_purchase_cooldown", "cancel_purchase_cooldown", "corporation_web_refresh_token", "structure_info_web_refresh_token"]
    PURCHASE_MAX_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    MAKE_PURCHASE_COOLDOWN_FIELD_NUMBER: _ClassVar[int]
    CANCEL_PURCHASE_COOLDOWN_FIELD_NUMBER: _ClassVar[int]
    CORPORATION_WEB_REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    STRUCTURE_INFO_WEB_REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    purchase_max_active: int
    make_purchase_cooldown: int
    cancel_purchase_cooldown: int
    corporation_web_refresh_token: str
    structure_info_web_refresh_token: str
    def __init__(self, purchase_max_active: _Optional[int] = ..., make_purchase_cooldown: _Optional[int] = ..., cancel_purchase_cooldown: _Optional[int] = ..., corporation_web_refresh_token: _Optional[str] = ..., structure_info_web_refresh_token: _Optional[str] = ...) -> None: ...

class CfgGetConstDataRequest(_message.Message):
    __slots__ = ["auth"]
    AUTH_FIELD_NUMBER: _ClassVar[int]
    auth: AuthRequest
    def __init__(self, auth: _Optional[_Union[AuthRequest, _Mapping]] = ...) -> None: ...

class CfgGetConstDataResponse(_message.Message):
    __slots__ = ["const_data", "auth", "error"]
    CONST_DATA_FIELD_NUMBER: _ClassVar[int]
    AUTH_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    const_data: ConstData
    auth: AuthResponse
    error: ErrorResponse
    def __init__(self, const_data: _Optional[_Union[ConstData, _Mapping]] = ..., auth: _Optional[_Union[AuthResponse, _Mapping]] = ..., error: _Optional[_Union[ErrorResponse, _Mapping]] = ...) -> None: ...

class CfgSetConstDataRequest(_message.Message):
    __slots__ = ["const_data", "auth"]
    CONST_DATA_FIELD_NUMBER: _ClassVar[int]
    AUTH_FIELD_NUMBER: _ClassVar[int]
    const_data: ConstData
    auth: AuthRequest
    def __init__(self, const_data: _Optional[_Union[ConstData, _Mapping]] = ..., auth: _Optional[_Union[AuthRequest, _Mapping]] = ...) -> None: ...

class CfgSetConstDataResponse(_message.Message):
    __slots__ = ["auth", "error"]
    AUTH_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    auth: AuthResponse
    error: ErrorResponse
    def __init__(self, auth: _Optional[_Union[AuthResponse, _Mapping]] = ..., error: _Optional[_Union[ErrorResponse, _Mapping]] = ...) -> None: ...

class IsAdminRequest(_message.Message):
    __slots__ = ["auth"]
    AUTH_FIELD_NUMBER: _ClassVar[int]
    auth: AuthRequest
    def __init__(self, auth: _Optional[_Union[AuthRequest, _Mapping]] = ...) -> None: ...

class IsAdminResponse(_message.Message):
    __slots__ = ["is_admin", "auth", "error"]
    IS_ADMIN_FIELD_NUMBER: _ClassVar[int]
    AUTH_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    is_admin: bool
    auth: AuthResponse
    error: ErrorResponse
    def __init__(self, is_admin: bool = ..., auth: _Optional[_Union[AuthResponse, _Mapping]] = ..., error: _Optional[_Union[ErrorResponse, _Mapping]] = ...) -> None: ...

class CharacterInfoRequest(_message.Message):
    __slots__ = ["character_id"]
    CHARACTER_ID_FIELD_NUMBER: _ClassVar[int]
    character_id: int
    def __init__(self, character_id: _Optional[int] = ...) -> None: ...

class CharacterInfoResponse(_message.Message):
    __slots__ = ["character_id", "corporation_id", "alliance_id", "name", "error"]
    CHARACTER_ID_FIELD_NUMBER: _ClassVar[int]
    CORPORATION_ID_FIELD_NUMBER: _ClassVar[int]
    ALLIANCE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    character_id: int
    corporation_id: int
    alliance_id: OptionalInt32
    name: str
    error: ErrorResponse
    def __init__(self, character_id: _Optional[int] = ..., corporation_id: _Optional[int] = ..., alliance_id: _Optional[_Union[OptionalInt32, _Mapping]] = ..., name: _Optional[str] = ..., error: _Optional[_Union[ErrorResponse, _Mapping]] = ...) -> None: ...

class CorporationInfoRequest(_message.Message):
    __slots__ = ["corporation_id"]
    CORPORATION_ID_FIELD_NUMBER: _ClassVar[int]
    corporation_id: int
    def __init__(self, corporation_id: _Optional[int] = ...) -> None: ...

class CorporationInfoResponse(_message.Message):
    __slots__ = ["corporation_id", "alliance_id", "name", "ticker", "error"]
    CORPORATION_ID_FIELD_NUMBER: _ClassVar[int]
    ALLIANCE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TICKER_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    corporation_id: int
    alliance_id: OptionalInt32
    name: str
    ticker: str
    error: ErrorResponse
    def __init__(self, corporation_id: _Optional[int] = ..., alliance_id: _Optional[_Union[OptionalInt32, _Mapping]] = ..., name: _Optional[str] = ..., ticker: _Optional[str] = ..., error: _Optional[_Union[ErrorResponse, _Mapping]] = ...) -> None: ...

class AllianceInfoRequest(_message.Message):
    __slots__ = ["alliance_id"]
    ALLIANCE_ID_FIELD_NUMBER: _ClassVar[int]
    alliance_id: int
    def __init__(self, alliance_id: _Optional[int] = ...) -> None: ...

class AllianceInfoResponse(_message.Message):
    __slots__ = ["alliance_id", "name", "ticker", "error"]
    ALLIANCE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TICKER_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    alliance_id: int
    name: str
    ticker: str
    error: ErrorResponse
    def __init__(self, alliance_id: _Optional[int] = ..., name: _Optional[str] = ..., ticker: _Optional[str] = ..., error: _Optional[_Union[ErrorResponse, _Mapping]] = ...) -> None: ...
