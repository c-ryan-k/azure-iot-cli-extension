# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azext_iot.product.providers.provider import get_sdk
from uuid import uuid4
from knack.util import CLIError
import os


def initialize_workspace(cmd, product_name, working_folder="PnPCert"):
    id = uuid4()
    if not os.path.exists(working_folder):
        os.mkdir(working_folder)

    product_config = {
        "id": str(id),
        "name": product_name,
        "industryTemplates": [
            "InstoreAnalytics |" +
            " DigitalDistributionCenter |" +
            " ConnectedLogistics |" +
            " SmartInventoryManagement |" +
            " ContinuousPatientMonitoring |" +
            " SmartMeterAnalytics |" +
            " SolarPowerMonitoring |" +
            " WaterQualityMonitoring |" +
            " WaterConsumptionMonitoring |" +
            " ConnectedWasteManagement |" +
            " ShelfAvailability"

        ],
        "shortDescription": "string - max length 100",
        "longDescription": "string - max length 1200",
        "dimensions": {
            "length": {
                "value": 0,
                "displayUnit": "cm | @in"
            },
            "width": {
                "value": 0,
                "displayUnit": "cm | @in"
            },
            "height": {
                "value": 0,
                "displayUnit": "cm | @in"
            }
        },
        "weight": {
            "value": 0,
            "displayUnit": "g | lb"
        },
        "deviceType": "FinishedProduct | DevKit",
        "geoAvailability": [
            "Worldwide | EMEA | APAC_Except_Japan | Americas | Japan"
        ],
        "marketingPage": "url",
        "purchaseURL": "url",
        "salesContact": "url",
        "caseStudyURL": "url",
        "languages": [
            "C | CSharp | Java | JavaScript | Python"
        ],
        "os": [""],
        "cloudProtocols": [
            "AMQPS | AMQPS_Websockets | MQTT | MQTT_Websockets | HTTPS"
        ],
        "industrialProtocols": [
            "CAN_Bus | EtherCAT | Modbus | OPC_Classic | OPC_UA | PROFINET | ZigBee | PPMP | Others"
        ],
        "connectivity": [
            "Bluetooth | LAN | WIFI | LTE | ThreeG | Others"
        ],
        "hardwareInterfaces": [
            "GPIO | I2C_SPI | COM | USB | Others"
        ],
        "integratedSensors": [
            "GPS |" +
            " Touch |" +
            " LED |" +
            " Light |" +
            " Gas |" +
            " Noise |" +
            " Proximity |" +
            " Temperature |" +
            " Humidity |" +
            " Pressure |" +
            " Accelerometers |" +
            " Weight |" +
            " Soil_Alkalinity |" +
            " Vibrations |" +
            " Image_capture |" +
            " Motion_Detection |" +
            " Chemical_compound_presence |" +
            " No_Sensors"
        ],
        "secureHardware": [
            "TPM | DICE | SIM_eSIM | Smartcard | Others"
        ],
        "numOfHardwareComponents": 1,
        "componentType": "SoM_SoC | Carrier_Board",
        "componentName": "Video_SoM | Audio_SoM | Video_Carrier_Board | Others",
        "processorArchitecture": "arm | arm64 | x86 | amd64",
        "processorManufacturer": "string",
        "totalStorage": {
            "value": 0,
            "displayUnit": "b | kb | mb | gb"
        },
        "totalMemory": {
            "value": 0,
            "displayUnit": "b | kb | mb | gb"
        },
        "battery": {
            "value": 0,
            "displayUnit": "mwH"
        },
        "hardwareAcceleratorManufacturer": "string",
        "hardwareAcceleratorName": "string",
        "hardwareAcceleratorVersion": "string",
        "industryCertifications": ["FCC | ISCC | Others"],
        "industryCertificationExternalLink": "url",
        "distributors": [
            {
                "name": "string",
                "purchaseUrl": "url"
            }
        ],
        "techSpecURL": "url",
        "firmwareImageURL": "url"
    }

    from json import dump
    from os import path
    with open(file=path.join(working_folder, "product_configuration.json"), mode='w+', encoding='utf-8') as f:
        dump(
            obj=product_config,
            fp=f,
            indent=4,
            sort_keys=False
        )


def create(cmd, configuration_file, provisioning=False):
    # call to POST /deviceTests
    return True


def show(cmd, test_id):
    # call to GET /deviceTests/{deviceTestId}
    return True


def update(cmd, test_id, configuration_file, provisioning=False):
    # call to POST /deviceTests
    return True


def search(cmd, product_id=None, registration_id=None, certificate_name=None):
    # call to POST /deviceTests/search
    if not any([product_id or registration_id or certificate_name]):
        raise CLIError('At least one search criteria must be specified')

    searchOptions = {
        'product_id': product_id,
        'dps_registration_id': registration_id,
        'dps_x509_certificate_common_name': certificate_name
    }

    return get_sdk(cmd).search_device_test(
        body=searchOptions
    )
