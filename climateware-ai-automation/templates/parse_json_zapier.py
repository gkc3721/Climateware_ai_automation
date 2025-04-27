import json

# input_data['json_text'] Zapier'den gelen JSON string olacak

data = json.loads(input_data['json_text'])

# Türkçe karakterler korunarak veriler dönülüyor
return {
    "project_title": data.get("project_title", ""),
    "project_goal": data.get("project_goal", ""),
    "outputs": data.get("outputs", ""),
    "co2_saving": data.get("co2_saving", ""),
    "co2_value": data.get("co2_value", ""),
    "next_step_1": data.get("next_steps", ["", "", ""])[0],
    "next_step_2": data.get("next_steps", ["", "", ""])[1],
    "next_step_3": data.get("next_steps", ["", "", ""])[2],
}
