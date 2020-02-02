'''
 Copyright (C) 2019 Maged Mokhtar <mmokhtar <at> petasan.org>
 Copyright (C) 2019 PetaSAN www.petasan.org


 This program is free software; you can redistribute it and/or
 modify it under the terms of the GNU Affero General Public License
 as published by the Free Software Foundation

 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 GNU Affero General Public License for more details.
'''

import pickle
from PetaSAN.backend.manage_disk import ManageDisk
from PetaSAN.core.config import app_conf
from PetaSAN.core.entity.disk_info import DiskMeta
from PetaSAN.core.common.log import logger
