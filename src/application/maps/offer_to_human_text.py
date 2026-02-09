from application.enums.offer_types import OfferType

OFFER_TYPE_TO_TEXT = {
    OfferType.MAINTENANCE: "car maintenance service",
    OfferType.REPAIR: "general car repair service",
    OfferType.DIAGNOSTICS: "car diagnostics service",

    OfferType.ENGINE_REPAIR: "engine repair service",
    OfferType.TRANSMISSION_REPAIR: "transmission repair service",
    OfferType.CLUTCH_REPAIR: "clutch repair service",
    OfferType.TIMING_BELT_REPLACEMENT: "timing belt replacement service",

    OfferType.BRAKE_SERVICE: "brake service",
    OfferType.BRAKE_FLUID_SERVICE: "brake fluid service",

    OfferType.SUSPENSION_REPAIR: "suspension repair service",
    OfferType.STEERING_REPAIR: "steering repair service",

    OfferType.ELECTRICAL: "car electrical repair service",
    OfferType.BATTERY_SERVICE: "battery service",
    OfferType.ALTERNATOR_REPAIR: "alternator repair service",
    OfferType.STARTER_REPAIR: "starter repair service",
    OfferType.LIGHTING_REPAIR: "car lighting repair service",

    OfferType.ECU_PROGRAMMING: "ECU programming service",

    OfferType.OIL_CHANGE: "oil change service",
    OfferType.FILTER_REPLACEMENT: "filter replacement service",
    OfferType.COOLANT_SERVICE: "coolant service",
    OfferType.TRANSMISSION_FLUID_SERVICE: "transmission fluid service",

    OfferType.TIRE_CHANGE: "tire change service",
    OfferType.TIRE_BALANCING: "tire balancing service",
    OfferType.WHEEL_ALIGNMENT: "wheel alignment service",
    OfferType.PUNCTURE_REPAIR: "tire puncture repair service",

    OfferType.EXHAUST_REPAIR: "exhaust repair service",
    OfferType.EMISSIONS_SERVICE: "emissions service",
    OfferType.CATALYTIC_CONVERTER_REPAIR: "catalytic converter repair service",

    OfferType.AC_SERVICE: "air conditioning service",
    OfferType.AC_REPAIR: "air conditioning repair service",
    OfferType.HEATING_REPAIR: "car heating repair service",

    OfferType.BODY_WORK: "car body work service",
    OfferType.PAINTING: "car painting service",
    OfferType.DENT_REMOVAL: "dent removal service",
    OfferType.WINDSHIELD_REPLACEMENT: "windshield replacement service",
    OfferType.RUST_REPAIR: "rust repair service",

    OfferType.INTERIOR_REPAIR: "car interior repair service",
    OfferType.UPHOLSTERY_REPAIR: "upholstery repair service",
    OfferType.WINDOW_MECHANISM_REPAIR: "window mechanism repair service",

    OfferType.PRE_PURCHASE_INSPECTION: "pre-purchase car inspection",
    OfferType.SAFETY_INSPECTION: "vehicle safety inspection",

    OfferType.CAR_WASH: "car wash service",
    OfferType.DETAILING: "car detailing service",

    OfferType.TOWING: "vehicle towing service",
}
