/**
 * @license
 * Copyright 2018-2020 Streamlit Inc.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *    http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

import React from "react"
import moment from "moment"
import { Datepicker as UIDatePicker } from "baseui/datepicker"
import { Map as ImmutableMap } from "immutable"
import { WidgetStateManager, Source } from "lib/WidgetStateManager"
import { datePickerOverrides } from "lib/widgetTheme"

export interface Props {
  disabled: boolean
  element: ImmutableMap<string, any>
  widgetMgr: WidgetStateManager
  width: number
}

interface State {
  /**
   * The value specified by the user via the UI. If the user didn't touch this
   * widget's UI, the default value is used.
   */
  value: string
}

class DateInput extends React.PureComponent<Props, State> {
  public state: State = {
    value: this.props.element.get("default"),
  }

  public componentDidMount(): void {
    this.setWidgetValue({ fromUi: false })
  }

  private setWidgetValue = (source: Source): void => {
    const widgetId: string = this.props.element.get("id")
    this.props.widgetMgr.setStringValue(widgetId, this.state.value, source)
  }

  private handleChange = ({ date }: { date: Date | Date[] }): void => {
    const value = moment(date as Date).format("YYYY/MM/DD")

    this.setState({ value }, () => this.setWidgetValue({ fromUi: true }))
  }

  private getMaxDate = (): Date | undefined => {
    const { element } = this.props
    const maxDate = element.get("max")

    return maxDate && maxDate.length > 0 ? new Date(maxDate) : undefined
  }

  public render = (): React.ReactNode => {
    const { width, element, disabled } = this.props
    const { value } = this.state

    const style = { width }
    const label = element.get("label")
    const minDate = new Date(element.get("min"))
    const maxDate = this.getMaxDate()

    return (
      <div className="Widget stDateInput" style={style}>
        <label>{label}</label>
        <UIDatePicker
          formatString="yyyy/MM/dd"
          disabled={disabled}
          onChange={this.handleChange}
          overrides={datePickerOverrides}
          value={new Date(value)}
          minDate={minDate}
          maxDate={maxDate}
        />
      </div>
    )
  }
}

export default DateInput
