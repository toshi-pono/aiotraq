import React from "react";
import type { Props } from "@theme/Admonition";
import DefaultAdmonitionTypes from "@theme-original/Admonition/Types";

function BorderAdmonition(props: Props) {
  return (
    <div style={{ border: "solid var(--ifm-color-primary)", padding: 4 }}>
      <div>{props.children}</div>
    </div>
  );
}

const AdmonitionTypes = {
  ...DefaultAdmonitionTypes,

  // Add all your custom admonition types here...
  // You can also override the default ones if you want
  border: BorderAdmonition,
};

export default AdmonitionTypes;
