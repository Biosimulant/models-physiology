# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Auto-generated CellML BioModule wrapper for Faber, Rudy, 2000.

Source: physiome:faber_rudy_2000
Original: https://models.physiomeproject.org/workspace/faber_rudy_2000
"""
from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, Optional, Set, TYPE_CHECKING

if TYPE_CHECKING:  # pragma: no cover - typing only
    from biosim import BioWorld

import biosim
from biosim.signals import BioSignal, SignalMetadata

class CellmlFaberRudy2000(biosim.BioModule):
    """BioModule wrapper for CellML model: Faber, Rudy, 2000."""

    def __init__(self, model_path: str = "data/faber_rudy_2000.cellml", min_dt: float = 0.01) -> None:
        self.min_dt = min_dt
        self._model_path = Path(__file__).parent.parent / model_path
        self._t = 0.0
        self._model = None
        self._outputs: Dict[str, BioSignal] = {}

    def setup(self, config: Optional[Dict[str, Any]] = None) -> None:
        import libcellml

        parser = libcellml.Parser()
        self._model = parser.parseModel(
            self._model_path.read_text(encoding="utf-8")
        )
        self._t = 0.0

    def reset(self) -> None:
        self._t = 0.0
        self._outputs = {}

    def inputs(self) -> Set[str]:
        return set()

    def outputs(self) -> Set[str]:
        return {"state"}

    def advance_to(self, t: float) -> None:
        """Advance simulation to time *t* using libcellml."""
        if self._model is None:
            self.setup()

        self._t = t

        state_data: Dict[str, Any] = {"t": t}
        state_data["component_count"] = self._model.componentCount()
        state_data["variable_count"] = sum(
            self._model.component(i).variableCount()
            for i in range(self._model.componentCount())
        )
        components = []
        for i in range(self._model.componentCount()):
            comp = self._model.component(i)
            variables = []
            for j in range(comp.variableCount()):
                var = comp.variable(j)
                variables.append({
                    "name": var.name(),
                    "units": var.units().name() if var.units() else None,
                    "initial_value": var.initialValue() if var.initialValue() else None,
                })
            components.append({"name": comp.name(), "variables": variables})
        state_data["components"] = components

        source_name = getattr(self, "_world_name", self.__class__.__name__)
        self._outputs = {
            "state": BioSignal(
                source=source_name,
                name="state",
                value=state_data,
                time=t,
                metadata=SignalMetadata(
                    description="CellML model state",
                    kind="state",
                ),
            )
        }

    def get_outputs(self) -> Dict[str, BioSignal]:
        return dict(self._outputs)

    def visualize(self) -> Optional[Dict[str, Any]]:
        """Generate visualization from CellML model structure."""
        if self._model is None:
            return None

        state = self._outputs.get("state")
        value = state.value if state and isinstance(getattr(state, "value", None), dict) else {}

        lines = [
            f"CellML Model: {self._model.name() or 'unnamed'}",
            f"Time: {self._t}s",
            f"Components: {value.get('component_count', 0)}",
            f"Variables: {value.get('variable_count', 0)}",
        ]

        return {
            "render": "text",
            "data": {"text": "\n".join(lines)},
            "description": "CellML model structure",
        }

# Canonical alias for stable entrypoint naming.
FaberRudy2000Faberrudy2000Model = CellmlFaberRudy2000
