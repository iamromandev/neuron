from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `provider` (
    `id` CHAR(36) NOT NULL PRIMARY KEY,
    `created_at` DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    `updated_at` DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `deleted_at` DATETIME(6),
    `status` VARCHAR(11) NOT NULL COMMENT 'ACTIVE: active\nDEGRADED: degraded\nDISABLED: disabled\nMAINTENANCE: maintenance' DEFAULT 'active',
    `name` VARCHAR(64) NOT NULL UNIQUE,
    `slug` VARCHAR(64) NOT NULL UNIQUE,
    `base_url` VARCHAR(128),
    `meta` JSON,
    KEY `idx_provider_created_1a0189` (`created_at`),
    KEY `idx_provider_updated_318c28` (`updated_at`),
    KEY `idx_provider_deleted_24350e` (`deleted_at`)
) CHARACTER SET utf8mb4 COMMENT='Provider';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS `provider`;"""


MODELS_STATE = (
    "eJztl29P2zAQxr9KlFdMQkjtEEJomhTabGSiLaKBTTAUubGbWjh2SGygQv3u87lN0iSlQF"
    "ftj8Sbtnnuzrn7PXXcPtmxwITtnaXinmKS2kfWk81RTPSHemjXslGSFAG4lmjETGqynDTK"
    "ZIpCqfUxYhnREiZZmNJEUsEhe3lJLEKdTnmkA1wxpiXF6Z0igRQRkRPT0/WNlinH5JFk+W"
    "VyG4wpYbjSMsWwptEDOU2MdnHhdb+YTLjdKAgFUzEvs5OpnAhepCtF8R7UQCwinKRIErw0"
    "DHS5mDuX5h1rQaaKFK3iUsBkjBQDJPanseIhkLDMneBl/7PdgLRgsQJPKDgAplwCi6fZfK"
    "pyZqPacKvOiXO+8/Hgg5lSZDJKTdAQsWemEEk0LzVcS5BhSmDsAMkm0K6OSBqT1VCrlTW4"
    "eFG6l3/YBHIurKGc09sMqa1HwAPOpoul1yD2vZ479J3eGQwSZ9kdM4Qc34VI26jTmrozd0"
    "ToTTLfPcUi1nfPP7Hg0roa9N26b0Wef2VDT0hJEXDxECC8RCFXc1I6s/RVJXhDX6uV777+"
    "TV8XzZe26ucx2czWauUWbF10++dc/U9czDms3Z6ZRFJlTQ87E5S6XMXGQ0+Pj3hIGl6W1T"
    "UfNa7tbMjyQC/OM33S03vSPMBsp+N7l+6RNU/4ybvu13On63aPLEyiFGGCteYNneNTo9EM"
    "2tBaz/H6vtt3+h1dHIPNhBfjvrzHY/QYMMIjOdGXrdaab8elc25OyFar5nh/EWmb0KzikH"
    "lf6c/q/ZXnb8eRl39f/OYTskLvYP8V9A72n6UHoSq9jKnoLfTy/Hd6EBuhjAQqZW8huFyz"
    "EcWXn+fNh8I2Mbbah6/Zw+3D5zcxxKokYyJRk+K34aC/mmKeXyN4wfVo15iGctdiNJM3/y"
    "TPNfhg4srZmFPb6Tk/6kA7p4Pj+qEHCxxruPCPbHy79FcChBEKbx9QioNGRLTFc7nNUNyO"
    "6wriKDKsYOLZ7BcrR7oH"
)
