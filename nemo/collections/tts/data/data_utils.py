# Copyright (c) 2022, NVIDIA CORPORATION & AFFILIATES.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json
import os
from pathlib import Path

import numpy as np


def get_sup_data_file_path(entry: dict, base_audio_path: Path, sup_data_path: Path) -> Path:
    audio_path = Path(entry["audio_filepath"])
    rel_audio_path = audio_path.relative_to(base_audio_path).with_suffix("")
    audio_id = str(rel_audio_path).replace(os.sep, "_")
    file_name = f"{audio_id}.pt"
    file_path = Path(os.path.join(sup_data_path, file_name))
    return file_path


def normalize_volume(audio: np.array, volume_level: float) -> np.array:
    """Apply peak normalization to the input audio.
    """
    if not (0.0 <= volume_level <= 1.0):
        raise ValueError(f"Volume must be in range [0.0, 1.0], received {volume_level}")

    max_sample = np.max(np.abs(audio))
    if max_sample == 0:
        return audio

    return volume_level * (audio / np.max(np.abs(audio)))
