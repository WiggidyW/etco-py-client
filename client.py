import grpc
import etco_pb2
import etco_pb2_grpc

from proto_error import raise_if_err, raise_if_unauthorized
import data

class EtcoClient():
    def __init__(
        self,
        channel,
    ):
        self.channel = channel
        self.stub = etco_pb2_grpc.EveTradingCoStub(channel)

    async def sde_type_data(self) -> list[int]:
        rep: etco_pb2.SDETypeDataResponse = await self.stub.SDETypeData(
            etco_pb2.SDETypeDataRequest()
        )
        raise_if_err(rep.error)
        return list(rep.types)
    
    async def named_sde_type_data(self) -> list[data.NamedItem]:
        rep: etco_pb2.NamedSDETypeDataResponse = await self.stub.NamedSDETypeData(
            etco_pb2.NamedSDETypeDataRequest(),
        )
        raise_if_err(rep.error)
        return [data.NamedItem(
            lists=rep.type_naming_lists,
            indexes=item.type_naming_indexes,
            type_id=item.type_id,
            quantity=0,
        ) for item in rep.types]
    
    async def shop_locations(
        self,
        include_location_info: bool = False,
        include_location_name: bool = False,
        include_system_name: bool = False,
        include_region_name: bool = False,
    ) -> list[data.NamedLocation]:
        rep: etco_pb2.ShopLocationsResponse = await self.stub.ShopLocations(
            etco_pb2.ShopLocationsRequest(
                include_location_info=include_location_info,
                include_location_naming=etco_pb2.IncludeLocationNaming(
                    include_location_name=include_location_name,
                    include_system_name=include_system_name,
                    include_region_name=include_region_name,
                ),
            ),
        )
        raise_if_err(rep.error)
        return [data.NamedLocation(
            maps=rep.location_naming_maps,
            info=location.location_info,
            location_id=location.location_id,
        ) for location in rep.locations]
    
    async def buyback_systems(
        self,
        include_system_name: bool = False,
        include_region_name: bool = False,
    ) -> list[data.NamedSystem]:
        rep: etco_pb2.BuybackSystemsResponse = await self.stub.BuybackSystems(
            etco_pb2.BuybackSystemsRequest(
                include_location_naming=etco_pb2.IncludeLocationNaming(
                    include_location_name=False,
                    include_system_name=include_system_name,
                    include_region_name=include_region_name,
                ),
            )
        )
        raise_if_err(rep.error)
        return [data.NamedSystem(
            maps=rep.location_naming_maps,
            system_id=system.system_id,
            region_id=system.region_id,
        ) for system in rep.systems]
    
    async def sde_systems(
        self,
        include_system_name: bool = False,
        include_region_name: bool = False,
    ) -> list[data.NamedSystem]:
        rep: etco_pb2.SDESystemsResponse = await self.stub.SDESystems(
            etco_pb2.SDESystemsRequest(
                include_location_naming=etco_pb2.IncludeLocationNaming(
                    include_location_name=False,
                    include_system_name=include_system_name,
                    include_region_name=include_region_name,
                ),
            )
        )
        raise_if_err(rep.error)
        return [data.NamedSystem(
            maps=rep.location_naming_maps,
            system_id=system.system_id,
            region_id=system.region_id,
        ) for system in rep.systems]
    
    async def parse(
        self,
        text: str,
    ) -> list[data.ParsedItem]:
        rep: etco_pb2.ParseResponse = await self.stub.Parse(
            etco_pb2.ParseRequest(
                text=text,
            )
        )
        raise_if_err(rep.error)
        parsed_items = []
        for item in rep.known_items:
            parsed_items.append(data.ParsedItem(item, True))
        for item in rep.unknown_items:
            parsed_items.append(data.ParsedItem(item, False))
        return parsed_items
    
    async def status_buyback_appraisal(
        self,
        token: str,
        code: str,
        include_items: bool = False,
        include_item_name: bool = False,
        include_item_group: bool = False,
        include_item_category: bool = False,
        include_item_market_groups: bool = False,
        include_location_info: bool = False,
        include_location_name: bool = False,
        include_system_name: bool = False,
        include_region_name: bool = False,
    ) -> data.BuybackAppraisalStatus:
        rep: etco_pb2.StatusBuybackAppraisalResponse = await self.stub.Parse(
            etco_pb2.StatusBuybackAppraisalRequest(
                auth=etco_pb2.AuthRequest(token),
                code=code,
                include_items=include_items,
                include_type_naming=etco_pb2.IncludeTypeNaming(
                    include_name=include_item_name,
                    include_group=include_item_group,
                    include_category=include_item_category,
                    include_market_groups=include_item_market_groups,
                ),
                include_location_info=include_location_info,
                include_location_naming=etco_pb2.IncludeLocationNaming(
                    include_location_name=include_location_name,
                    include_system_name=include_system_name,
                    include_region_name=include_region_name,
                ),
            ),
        )
        raise_if_unauthorized(rep.auth)
        raise_if_err(rep.error)
        return data.BuybackAppraisalStatus(rep)
