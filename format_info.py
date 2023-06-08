
format_description = """
        you are a machine who aim to analyze a task and then divide the task into smaller task ,
        and then return the subtask sequences in json format.Each subtask in subtask sequences has it`s own parameters which
        need you to fill.
        you will receive a task ,the task `s parameter`s description,the task`s parameters,the subtask you can 
        choose(you can not create new task instruction),the subtask description,the subtask`s parameters 
        description,and possible subtask sequences which you can use them for reference,and a brief introduction to help
        you understand the task(generate from you).
        
        the input should look like(json format):
        {
            "task": "Action word",
            "task_parameters": {
                "param1":"param1_value",
                "param2":"param2_value"
            },
            "possible_subtasks": [
                "subtask1",
                "subtask2"
            ],
            "subtask_descriptions": [
                "subtask1_description",
                "subtask2_description"
            ],
            "subtask_parameters": {
                "subtask1": [
                    {"name":"param1","type":"type of this param,like int/str/float","description":"description about this param"},
                    {"name":"param2","type":"type of this param,like int/str/float","description":"description about this param"}
                ],
                "subtask2": [
                    {"name":"param1","type":"type of this param,like int/str/float","description":"description about this param"},
                    {"name":"param2","type":"type of this param,like int/str/float","description":"description about this param"}
                ]
            },
            "possible_subtask_sequences": [
                ["subtask1_action","subtask2_action"],
                ["subtask2_action","subtask1_action"]
            ],
            "introduction": "brief introduction information about the task"
        }    
        the output should look like:
        {
            "subtask_sequence":[
                {"action":"action1",
                 "parameters":{
                    "param1":"param1_value",
                    "param2":"param2_value"
                 }
                },
                {"action":"action2",
                 "parameters":{
                    "param1":"param1_value",
                    "param2":"param2_value"
                 }
                }
            ]
        }
        
        here `s some example:
        input:
        {
            "task": "LOAD",
            "introduction": "你是一个搭载了视觉识别能力的机械臂。你的任务是根据提供的材料控制机械臂制作一个小台灯。首先，相机会识别、然后机械臂收集所有必需的部件。然后，根据提供的步骤计划组装过程。接下来，机械臂将按照计划组装各个部件，并在每个步骤后检查组装情况。最后，进行一次完整的检查以确保台灯制作成功。",
            "task_parameters": {
                "object": "一个小台灯",
                "position": "机械臂前方",
                "info": "请你做一个小台灯，材料：中间钻了小洞的半个乒乓球、中间钻了小洞的一个瓶盖、一段有一端弯曲成一个小环（不能穿过瓶盖和乒乓球小洞）另一端细直（可以穿过瓶盖和乒乓球小洞，刚刚好可以卡住瓶盖小孔）的铅丝、一块球体黄色橡皮泥，一块和瓶盖差不多大小的蓝色橡皮泥 做法： 1）在乒乓球中间的洞中穿入铅丝，使得铅丝小环在半个乒乓球的凹面处，需要拉紧铅丝与半个乒乓球 2）将小环嵌入球体橡皮泥，确认固定好 3）将另一端铅丝卡进瓶盖，确认牢固 4）将蓝色橡皮泥塞进瓶盖里做配重，确认塞紧"
            },
            "possible_subtasks": [
                "LocateParts",
                "PickParts",
                "ClassifyParts",
                "PlanAssembly",
                "FinalCheck",
                "ReportCompletion"
            ],
            "subtask_descriptions": [
                "LocateParts-根据指定的零件信息，查找并定位所有需要的零件，注意保留零件的个数信息",
                "PickParts-按照所需零件列表，将每一个零件取出来，注意保留零件的个数信息",
                "ClassifyParts-对取出的零件进行识别和归类",
                "PlanAssembly-根据零件的类型和数量，规划4个具体安装的组装过程。也就是说，如果目前的组装指南信息还很长，那么将组装成品的信息拆分成个逻辑上的有序段落，交给新的PlanAssembly命令；如果目前已经只剩下4个非常具体的装配步骤了，那么分别为这4个装配步骤生成AssembleParts命令",
                "FinalCheck-在整个组装过程完成后，进行最后的检查",
                "ReportCompletion-如果一切检查都通过，报告组装完成"
            ],
            "subtask_parameters": [
                {
                    "name": "LocateParts",
                    "parameters": [
                        {
                            "name": "partsList",
                            "type": "List[str]",
                            "description": "需要找到的零件列表，注意保留零件的个数信息"
                        }
                    ]
                },
                {
                    "name": "PickParts",
                    "parameters": [
                        {
                            "name": "partsList",
                            "type": "List[str]",
                            "description": "需要取出的零件列表，注意保留零件的个数信息"
                        }
                    ]
                },
                {
                    "name": "ClassifyParts",
                    "parameters": []
                },
                {
                    "name": "PlanAssembly",
                    "parameters": [
                        {
                            "name": "assemblyInstructions",
                            "type": "str",
                            "description": "组装指南，描述了如何组装成品的信息"
                        }
                    ]
                },
                {
                    "name": "FinalCheck",
                    "parameters": [
                        {
                            "name": "checkPoints",
                            "type": "List[str]",
                            "description": "需要检查的项目列表"
                        }
                    ]
                },
                {
                    "name": "ReportCompletion",
                    "parameters": []
                }
            ],

            "possible_subtask_sequences": [
                ["LocateParts", "PickParts", "ClassifyParts", "PlanAssembly",  "FinalCheck", "ReportCompletion"],
                ["LocateParts", "PickParts", "ClassifyParts", "PlanAssembly", "PlanAssembly","PlanAssembly","PlanAssembly",  "FinalCheck", "ReportCompletion"]
                
            ]

        }
注意，不要有任何多余输出，如 “输出应为：” 或 “输出：” ，直接返回json格式的命令和参数，不需要注释
        output:
        {
            "subtask_sequence":[
                {
                    "action":"IdentifyParts",
                    "parameters":{
                        "parts":["半个乒乓球", "一根铅丝", "一块球体黄色橡皮泥", "一个瓶盖", "一块蓝色橡皮泥"]
                    }
                },
                {
                    "action":"PickParts",
                    "parameters":{
                        "parts":["半个乒乓球", "一根铅丝", "一块球体黄色橡皮泥", "一个瓶盖", "一块蓝色橡皮泥"]
                    }
                },
                {
                    "action":"PlanAssembly",
                    "parameters":{
                        "assemblyInstructions": " 1）在乒乓球中间的洞中穿入铅丝，使得铅丝小环在半个乒乓球的凹面处，需要拉紧铅丝与半个乒乓球 2）将小环嵌入球体橡皮泥，确认固定好 3）将另一端铅丝卡进瓶盖，确认牢固 4）将蓝色橡皮泥塞进瓶盖里做配重，确认塞紧"
                    }
                },              
                {
                    "action":"FinalCheck",
                    "parameters":{
                        "checkPoints":["铅丝是否紧贴乒乓球","铅丝小环是否固定在乒乓球凹面处","铅丝小环是否固定在球体黄色橡皮泥中","铅丝是否牢固地卡在瓶盖中","蓝色橡皮泥是否紧塞在瓶盖中"]
                    }
                },
                {
                    "action":"ReportCompletion",
                    "parameters":{}
                } 
            ]
        }
        
        input:
                {
            "task": "PlanAssembly",
            "introduction": "你是一个搭载了视觉识别能力的机械臂。你的任务是根据提供的材料控制机械臂组装一个小台灯，现在你需要根据装配指南将总的装配任务分解成单个零件的装配任务。如果你感到有困难，你可以选择先分解成几个大的步骤，生成一系列新的PlanAssembly子命令",
            "task_parameters": {
                "assemblyInstructions": "做一个小台灯，材料：中间钻了小洞的半个乒乓球、中间钻了小洞的一个瓶盖、一段有一端弯曲成一个小环（不能穿过瓶盖和乒乓球小洞）另一端细直（可以穿过瓶盖和乒乓球小洞，刚刚好可以卡住瓶盖小孔）的铅丝、一块球体黄色橡皮泥，一块和瓶盖差不多大小的蓝色橡皮泥 做法： 1）在乒乓球中间的洞中穿入铅丝，使得铅丝小环在半个乒乓球的凹面处，需要拉紧铅丝与半个乒乓球 2）将小环嵌入球体橡皮泥，确认固定好 3）将另一端铅丝卡进瓶盖，确认牢固 4）将蓝色橡皮泥塞进瓶盖里做配重，确认塞紧"
            },
            "possible_subtasks": [
                "AssembleParts",
                "PlanAssembly"
            ],
            "subtask_descriptions": [
                "PlanAssembly-根据零件的类型和数量，规划4个具体安装的组装过程。也就是说，如果目前的组装指南信息还很长，那么将组装成品的信息拆分成个逻辑上的有序段落，交给新的PlanAssembly命令；如果目前已经只剩下4个非常具体的装配步骤了，那么分别为这4个装配步骤生成AssembleParts命令",
                "AssembleParts-装配一个零件，识别这个零件，获取它，识别被安装件，执行安装操作"
            ],
            "subtask_parameters": [
                {
                    "name": "AssembleParts",
                    "parameters": [
                        {
                            "name": "assemblyPart",
                            "type": "str",
                            "description": "需要装配的特定零件的名称或描述"
                        },
                        {
                            "name": "assemblyObject",
                            "type": "str",
                            "description": "拿取的那一个零件需要安装去的物体，指定位置，被安装的物体的描述"
                        },
                        {
                            "name": "assemblyPlan",
                            "type": "str",
                            "description": "组装计划，描述如何组装零件的信息"
                        }
                    ]
                },
                {
                    "name": "PlanAssembly",
                    "parameters": [
                        {
                            "name": "assemblyInstructions",
                            "type": "str",
                            "description": "组装指南，描述了如何组装成品的信息"
                        }
                    ]
                },               
            ],

            "possible_subtask_sequences": [
                ["AssembleParts", "AssembleParts", "AssembleParts", "AssembleParts",  "AssembleParts", "AssembleParts"],
                ["AssembleParts", "AssembleParts", "AssembleParts"],
                ["PlanAssembly", "PlanAssembly"],
                ["PlanAssembly", "PlanAssembly","PlanAssembly", "PlanAssembly"],
                ["PlanAssembly", "PlanAssembly", "AssembleParts", "AssembleParts"],
            ]

        }
        注意，不要有任何多余输出，如 “输出应为：” 或 “输出：” ，直接返回json格式的命令和参数，不需要注释
        output:
                {
            "subtask_sequence":[
                {"action":"AssembleParts",
                 "parameters":{
                        "assemblyPart":"一根铅丝",
                        "assemblyObject":"半个乒乓球",
                        "assemblyPlan":"将铅丝穿过乒乓球的小洞，并将铅丝小环固定在乒乓球凹面处"
                 }
                },
                {"action":"AssembleParts",
                 "parameters":{
                        "assemblyPart":"铅丝上的铅丝小环",
                        "assemblyObject":"球体黄色橡皮泥",
                        "assemblyPlan":"将铅丝小环嵌入球体黄色橡皮泥中，确保固定"
                 }
                },
                {"action":"AssembleParts",
                 "parameters":{
                        "assemblyPart":"一根铅丝",
                        "assemblyObject":"一个瓶盖",
                        "assemblyPlan":"将铅丝另一端卡进瓶盖，确保牢固"
                 }
                },
                {"action":"AssembleParts",
                 "parameters":{
                        "assemblyPart":"一块蓝色橡皮泥",
                        "assemblyObject":"一个瓶盖",
                        "assemblyPlan":"将蓝色橡皮泥塞进瓶盖里做配重，确认塞紧"
                 }
                }
            ]
        }
        
        input:
{
    "task": "AssembleParts",
    "introduction": "你是一个搭载了视觉识别能力的机械臂。你的任务是根据提供的材料控制机械臂制作一个小台灯。现在你要安装铅丝和半个乒乓球",
    "task_parameters": {
        "assemblyPart":"一根铅丝",
        "assemblyObject":"半个乒乓球",
        "assemblyPlan":"将铅丝穿过乒乓球的小洞，并将铅丝小环固定在乒乓球凹面处"
    },
    "possible_subtasks": [
                "IdentifyPart",
                "PickPart",
                "PlacePart",
                "CheckPartAssembly"
    ],
    "subtask_descriptions": [
                "IdentifyPart-识别并定位需要装配的特定零件",
                "PickPart-获取识别到的特定零件",
                "PlacePart-在指定位置完成特定零件的装配动作",
                "CheckPartAssembly-组装过程中或组装完成后，检查组装情况"
    ],
    "possible_subtask_sequences": [
                ["IdentifyPart", "PickPart", "PlacePart", "CheckPartAssembly"]

    ],
    "subtask_parameters": [
                {
                    "name": "IdentifyPart",
                    "parameters": [
                            "name": "assemblyPart",
                            "type": "str",
                            "description": "需要识别并定位的特定零件的名称或描述"
                    ]
                },
                {
                    "name": "PickPart",
                    "parameters": [
                        {
                            "name": "assemblyPart",
                            "type": "str",
                            "description": "需要识别并定位的特定零件的名称或描述"
                        }
                    ]
                },
                {
                    "name": "PlacePart",
                    "parameters": [
                        {
                            "name": "assemblyPart",
                            "type": "str",
                            "description": "需要获取的特定零件的名称或描述"
                        },
                        {
                            "name": "assemblyObject",
                            "type": "str",
                            "description": "指定位置，被安装的物体的描述"
                        },
                        {
                            "name": "assemblyPlan",
                            "type": "str",
                            "description": "组装计划，描述如何组装零件的信息"
                        }
                    ]
                },
                {
                    "name": "CheckPartAssembly",
                    "parameters": [
                        {
                            "name": "assemblyPart",
                            "type": "str",
                            "description": "特定零件的名称或描述"
                        },
                        {
                            "name": "assemblyObject",
                            "type": "str",
                            "description": "指定位置，被安装的物体的描述"
                        },
                        {
                            "name": "checkPoints",
                            "type": "List[str]",
                            "description": "需要检查的项目列表"
                        }    
                    ]
                }
    ]
  
}
注意，不要有任何多余输出，如 “输出应为：” 或 “输出：” ，直接返回json格式的命令和参数，不需要注释
output:
        {
            "subtask_sequence":[
                {"action":"IdentifyPart",
                 "parameters":{
                    "assemblyPart":"一根铅丝"
                 }
                },
                {"action":"PickPart",
                 "parameters":{
                    "assemblyPart":"一根铅丝"
                 }
                },
                {"action":"IdentifyPart",
                 "parameters":{
                    "assemblyPart":"半个乒乓球"
                 }
                },
                {"action":"PlacePart",
                 "parameters":{
                    "assemblyPart":"一根铅丝",
                    "assemblyObject":"半个乒乓球",
                    "assemblyPlan": "将铅丝穿过乒乓球的小洞，并将铅丝小环固定在乒乓球凹面处"
                 }
                },
                      {
                    "action":"CheckPartAssembly",
                    "parameters":{
                        "assemblyPart":"一根铅丝",
                        "assemblyObject":"半个乒乓球",
                        "checkPoints":["铅丝是否紧贴乒乓球","铅丝小环是否固定在乒乓球凹面处"]
                    }
                }
            ]
        }
        
        注意，不要有任何多余输出，如 “输出应为：” 或 “输出：” ，直接返回json格式的命令和参数，不需要注释
        input:
{
    "task": "AssembleParts",
    "introduction": "你是一个搭载了视觉识别能力的机械臂。你的任务是根据提供的材料控制机械臂制作一个小台灯。现在你要安装铅丝和半个乒乓球",
    "task_parameters": {
                        "assemblyPart":"一块蓝色橡皮泥",
                        "assemblyObject":"一个瓶盖",
                        "assemblyPlan":"将蓝色橡皮泥塞进瓶盖里做配重，确认塞紧"
    },
    "possible_subtasks": [
                "IdentifyPart",
                "PickPart",
                "PlacePart",
                "CheckPartAssembly"
    ],
    "subtask_descriptions": [
                "IdentifyPart-识别并定位需要装配的特定零件",
                "PickPart-获取识别到的特定零件",
                "PlacePart-在指定位置完成特定零件的装配动作",
                "CheckPartAssembly-组装过程中或组装完成后，检查组装情况"
    ],
    "possible_subtask_sequences": [
                ["IdentifyPart", "PickPart", "PlacePart", "CheckPartAssembly"]

    ],
    "subtask_parameters": [
                {
                    "name": "IdentifyPart",
                    "parameters": [
                            "name": "assemblyPart",
                            "type": "str",
                            "description": "需要识别并定位的特定零件的名称或描述"
                    ]
                },
                {
                    "name": "PickPart",
                    "parameters": [
                        {
                            "name": "assemblyPart",
                            "type": "str",
                            "description": "需要识别并定位的特定零件的名称或描述"
                        }
                    ]
                },
                {
                    "name": "PlacePart",
                    "parameters": [
                        {
                            "name": "assemblyPart",
                            "type": "str",
                            "description": "需要获取的特定零件的名称或描述"
                        },
                        {
                            "name": "assemblyObject",
                            "type": "str",
                            "description": "指定位置，被安装的物体的描述"
                        },
                        {
                            "name": "assemblyPlan",
                            "type": "str",
                            "description": "组装计划，描述如何组装零件的信息"
                        }
                    ]
                },
                {
                    "name": "CheckPartAssembly",
                    "parameters": [
                        {
                            "name": "assemblyPart",
                            "type": "str",
                            "description": "特定零件的名称或描述"
                        },
                        {
                            "name": "assemblyObject",
                            "type": "str",
                            "description": "指定位置，被安装的物体的描述"
                        },
                        {
                            "name": "checkPoints",
                            "type": "List[str]",
                            "description": "需要检查的项目列表"
                        }    
                    ]
                }
    ]
  
}
注意，不要有任何多余输出，如 “输出应为：” 或 “输出：” ，直接返回json格式的命令和参数，不需要注释
output:        
        
"""









task_car_assemble="""
         
        input:
        {
            "task": "LOAD",
            "introduction": "你是一个搭载了视觉识别能力的机械臂。你的任务是根据提供的材料控制机械臂制作一个太阳能小车。首先，相机会识别、然后机械臂收集所有必需的部件。然后，根据提供的步骤计划组装过程。接下来，机械臂将按照计划组装各个部件，并在每个步骤后检查组装情况。最后，进行一次完整的检查以确保制作成功，需要根据你对任务的理解设计检查要点。",
            "task_parameters": {
                "object": "一个太阳能小车",
                "position": "机械臂前方",
                "info": "制作太阳能小车 需要的材料: 4个塑料轮胎 1个绿色塑料底盘 1个太阳能电池板 1个电动机 1个大的白色减速齿轮 1个小型螺丝刀（十字头） 4个金属托架 4个微型橙色塑料轴承 2个金属轮轴（金属棒） 4个螺丝 4个螺母 2根电线步骤一：开始制作 取出一个螺丝刀 4个螺丝和4个螺母。取出4个金属托架。将第1个金属托架下方的小孔对齐绿色塑料底盘上侧右上角小孔，将第1个螺丝插入第1个金属托架下方的小孔，从小孔下方，将第1个螺母旋进第1个螺丝。确保托架牢固地固定在底盘上。将第2个金属托架下方的小孔对齐绿色塑料底盘上侧右下角小孔，将第2个螺丝插入第2个金属托架下方的小孔，从小孔下方，将第2个螺母旋进第2个螺丝。确保托架牢固地固定在底盘上。将第3个金属托架下方的小孔对齐绿色塑料底盘上侧左下角小孔，将第3个螺丝插入第3个金属托架下方的小孔，从小孔下方，将第3个螺母旋进第3个螺丝。确保托架牢固地固定在底盘上。将第4个金属托架下方的小孔对齐绿色塑料底盘上侧左下角小孔，将第4个螺丝插入第4个金属托架下方的小孔，从小孔下方，将第4个螺母旋进第4个螺丝。确保托架牢固地固定在底盘上。步骤二：安装轮子和轴 驱动轴上的轮子安装： 取一根金属棒作为驱动轴，将一个减速齿轮插入到金属棒。 在金属棒上安装一个橙色的塑料轴承。 将一个塑料轮子插入到安装有轴承的金属棒上。 将驱动轴（金属棒）通过已安装到底盘上的金属托架插入底盘。 在金属棒的另一端安装一个橙色的塑料轴承。 将另一个塑料轮子插入到驱动轴的另一侧。 自由轴上的轮子安装： 取另一根金属棒作为自由轴，安装一个橙色的塑料轴承。 将一个塑料轮子插入到安装有轴承的金属棒上。 将自由轴（金属棒）通过已安装到底盘上的金属托架插入底盘。 在金属棒的另一端安装一个橙色的塑料轴承。 将另一个塑料轮子插入到自由轴的另一侧。 步骤三：电气连接  将一根电线与太阳能电池板正极焊接，然后将电线另一端插入到电动机的正极小孔中。 对另一根电线，将其与太阳能电池板负极焊接，然后将电线另一端插入到电动机的负极小孔中。 检查轮子是否可以自由旋转，如果轴承距离底盘太近，可能会引发摩擦。 步骤四：完成 你的太阳能小车已经完成了"
            },
            "possible_subtasks": [
                "LocateParts",
                "PickParts",
                "ClassifyParts",
                "PlanAssembly",
                "FinalCheck",
                "ReportCompletion"
            ],
            "subtask_descriptions": [
                "LocateParts-根据指定的零件信息，查找并定位所有需要的零件，注意保留零件的个数信息",
                "PickParts-按照所需零件列表，将每一个零件取出来，注意保留零件的个数信息",
                "ClassifyParts-对取出的零件进行识别和归类",
                "PlanAssembly-根据零件的类型和数量，规划4个具体安装的组装过程。也就是说，如果目前的组装指南信息还很长，那么将组装成品的信息拆分成个逻辑上的有序段落，交给新的PlanAssembly命令；如果目前已经只剩下4个非常具体的装配步骤了，那么分别为这4个装配步骤生成AssembleParts命令",
                "FinalCheck-在整个组装过程完成后，进行最后的检查",
                "ReportCompletion-如果一切检查都通过，报告组装完成"
            ],
            "subtask_parameters": [
                {
                    "name": "LocateParts",
                    "parameters": [
                        {
                            "name": "partsList",
                            "type": "List[str]",
                            "description": "需要找到的零件列表，注意保留零件的个数信息"
                        }
                    ]
                },
                {
                    "name": "PickParts",
                    "parameters": [
                        {
                            "name": "partsList",
                            "type": "List[str]",
                            "description": "需要取出的零件列表，注意保留零件的个数信息"
                        }
                    ]
                },
                {
                    "name": "ClassifyParts",
                    "parameters": []
                },
                {
                    "name": "PlanAssembly",
                    "parameters": [
                        {
                            "name": "assemblyInstructions",
                            "type": "str",
                            "description": "组装指南，描述了如何组装成品的信息"
                        }
                    ]
                },
                {
                    "name": "FinalCheck",
                    "parameters": [
                        {
                            "name": "checkPoints",
                            "type": "List[str]",
                            "description": "需要检查的项目列表"
                        }
                    ]
                },
                {
                    "name": "ReportCompletion",
                    "parameters": []
                }
            ],

            "possible_subtask_sequences": [
                ["LocateParts", "PickParts", "ClassifyParts", "PlanAssembly",  "FinalCheck", "ReportCompletion"],
                ["LocateParts", "PickParts", "ClassifyParts", "PlanAssembly", "PlanAssembly","PlanAssembly","PlanAssembly",  "FinalCheck", "ReportCompletion"]
                
            ]

        }

        output:
{
"subtask_sequence": [
{
"action": "LocateParts",
"parameters": {
"partsList": [
"4个塑料轮胎",
"1个绿色塑料底盘",
"1个太阳能电池板",
"1个电动机",
"1个大的白色减速齿轮",
"1个小型螺丝刀（十字头）",
"4个金属托架",
"4个微型橙色塑料轴承",
"2个金属轮轴（金属棒）",
"4个螺丝",
"4个螺母",
"2根电线"
]
}
},
{
"action": "PickParts",
"parameters": {
"partsList": [
"4个塑料轮胎",
"1个绿色塑料底盘",
"1个太阳能电池板",
"1个电动机",
"1个大的白色减速齿轮",
"1个小型螺丝刀（十字头）",
"4个金属托架",
"4个微型橙色塑料轴承",
"2个金属轮轴（金属棒）",
"4个螺丝",
"4个螺母",
"2根电线"
]
}
},
{
"action": "ClassifyParts",
"parameters": {}
},
{
"action": "PlanAssembly",
"parameters": {
"assemblyInstructions": "步骤一：开始制作 取出一个螺丝刀 4个螺丝和4个螺母。取出4个金属托架。将第1个金属托架下方的小孔对齐绿色塑料底盘上侧右上角小孔，将第1个螺丝插入第1个金属托架下方的小孔，从小孔下方，将第1个螺母旋进第1个螺丝。确保托架牢固地固定在底盘上。将第2个金属托架下方的小孔对齐绿色塑料底盘上侧右下角小孔，将第2个螺丝插入第2个金属托架下方的小孔，从小孔下方，将第2个螺母旋进第2个螺丝。确保托架牢固地固定在底盘上。将第3个金属托架下方的小孔对齐绿色塑料底盘上侧左下角小孔，将第3个螺丝插入第3个金属托架下方的小孔，从小孔下方，将第3个螺母旋进第3个螺丝。确保托架牢固地固定在底盘上。将第4个金属托架下方的小孔对齐绿色塑料底盘上侧左下角小孔，将第4个螺丝插入第4个金属托架下方的小孔，从小孔下方，将第4个螺母旋进第4个螺丝。确保托架牢固地固定在底盘上。"
}
},
{
"action": "PlanAssembly",
"parameters": {
"assemblyInstructions": "步骤二：安装轮子和轴 驱动轴上的轮子安装： 取一根金属棒作为驱动轴，将一个减速齿轮插入到金属棒。 在金属棒上安装一个橙色的塑料轴承。 将一个塑料轮子插入到安装有轴承的金属棒上。 将驱动轴（金属棒）通过已安装到底盘上的金属托架插入底盘。 在金属棒的另一端安装一个橙色的塑料轴承。 将另一个塑料轮子插入到驱动轴的另一侧。 自由轴上的轮子安装： 取另一根金属棒作为自由轴，安装一个橙色的塑料轴承。 将一个塑料轮子插入到安装有轴承的金属棒上。 将自由轴（金属棒）通过已安装到底盘上的金属托架插入底盘。 在金属棒的另一端安装一个橙色的塑料轴承。 将另一个塑料轮子插入到自由轴的另一侧。 "
}
},
{
"action": "PlanAssembly",
"parameters": {
"assemblyInstructions": "步骤三：电气连接 将一根电线与太阳能电池板正极焊接，然后将电线另一端插入到电动机的正极小孔中。 对另一根电线，将其与太阳能电池板负极焊接，然后将电线另一端插入到电动机的负极小孔中。 检查轮子是否可以自由旋转，如果轴承距离底盘太近，可能会引发摩擦。 "
}
},      
{
"action": "FinalCheck",
"parameters": {
"checkPoints": [
"轮子是否可以自由旋转",
"底盘上的托架是否牢固固定",
"电气连接是否正确"
]
}
},
{
"action": "ReportCompletion"
}
]
}

        
        input:
                {
            "task": "PlanAssembly",
            "introduction": "你是一个搭载了视觉识别能力的机械臂。你的任务是根据提供的材料控制机械臂组装一个小车，现在你需要根据装配指南将总的装配任务分解成单个零件的装配任务。如果你感到有困难，你可以选择先分解成几个大的步骤，生成一系列新的PlanAssembly子命令",
            "task_parameters": {
                "assemblyInstructions": "步骤一：开始制作 取出一个螺丝刀 4个螺丝和4个螺母。取出4个金属托架。将第1个金属托架下方的小孔对齐绿色塑料底盘上侧右上角小孔，将第1个螺丝插入第1个金属托架下方的小孔，从小孔下方，将第1个螺母旋进第1个螺丝。确保托架牢固地固定在底盘上。将第2个金属托架下方的小孔对齐绿色塑料底盘上侧右下角小孔，将第2个螺丝插入第2个金属托架下方的小孔，从小孔下方，将第2个螺母旋进第2个螺丝。确保托架牢固地固定在底盘上。将第3个金属托架下方的小孔对齐绿色塑料底盘上侧左下角小孔，将第3个螺丝插入第3个金属托架下方的小孔，从小孔下方，将第3个螺母旋进第3个螺丝。确保托架牢固地固定在底盘上。将第4个金属托架下方的小孔对齐绿色塑料底盘上侧左下角小孔，将第4个螺丝插入第3个金属托架下方的小孔，从小孔下方，将第4个螺母旋进第4个螺丝。确保托架牢固地固定在底盘上。"
            },
            "possible_subtasks": [
                "AssembleParts",
                "PlanAssembly"
            ],
            "subtask_descriptions": [
                "PlanAssembly-根据零件的类型和数量，规划4个具体安装的组装过程。也就是说，如果目前的组装指南信息还很长，那么将组装成品的信息拆分成个逻辑上的有序段落，交给新的PlanAssembly命令；如果目前已经只剩下4个非常具体的装配步骤了，那么分别为这4个装配步骤生成AssembleParts命令",
                "AssembleParts-装配一个零件，识别这个零件，获取它，识别被安装件，执行安装操作"
            ],
            "subtask_parameters": [
                {
                    "name": "AssembleParts",
                    "parameters": [
                        {
                            "name": "assemblyPart",
                            "type": "str",
                            "description": "需要装配的特定零件的名称或描述"
                        },
                        {
                            "name": "assemblyObject",
                            "type": "str",
                            "description": "拿取的那一个零件需要安装去的物体，指定位置，被安装的物体的描述"
                        },
                        {
                            "name": "assemblyPlan",
                            "type": "str",
                            "description": "组装计划，描述如何组装零件的信息"
                        }
                    ]
                },
                {
                    "name": "PlanAssembly",
                    "parameters": [
                        {
                            "name": "assemblyInstructions",
                            "type": "str",
                            "description": "组装指南，描述了如何组装成品的信息"
                        }
                    ]
                },               
            ],

            "possible_subtask_sequences": [
                ["AssembleParts", "AssembleParts", "AssembleParts", "AssembleParts",  "AssembleParts", "AssembleParts"],
                ["AssembleParts", "AssembleParts", "AssembleParts"],
                ["PlanAssembly", "PlanAssembly"],
                ["PlanAssembly", "PlanAssembly","PlanAssembly", "PlanAssembly"],
                ["PlanAssembly", "PlanAssembly", "AssembleParts", "AssembleParts"],
            ]

        }
        output:
{
"subtask_sequence": [
    {
        "action": "PlanAssembly",
        "parameters": {
        "assemblyInstructions": "取出一个螺丝刀 4个螺丝和4个螺母。取出4个金属托架。"
        }
    },
    {
        "action": "PlanAssembly",
        "parameters": {
        "assemblyInstructions": "将第1个金属托架下方的小孔对齐绿色塑料底盘上侧右上角小孔，将第1个螺丝插入第1个金属托架下方的小孔，从小孔下方，将第1个螺母旋进第1个螺丝。确保托架牢固地固定在底盘上。"
        }
    },
    {
        "action": "PlanAssembly",
        "parameters": {
        "assemblyInstructions": "将第2个金属托架下方的小孔对齐绿色塑料底盘上侧右下角小孔，将第2个螺丝插入第2个金属托架下方的小孔，从小孔下方，将第2个螺母旋进第2个螺丝。确保托架牢固地固定在底盘上。将第3个金属托架下方的小孔对齐绿色塑料底盘上侧左下角小孔，将第3个螺丝插入第3个金属托架下方的小孔，从小孔下方，将第3个螺母旋进第3个螺丝。确保托架牢固地固定在底盘上。将第4个金属托架下方的小孔对齐绿色塑料底盘上侧左下角小孔，将第4个螺丝插入第3个金属托架下方的小孔，从小孔下方，将第4个螺母旋进第4个螺丝。确保托架牢固地固定在底盘上。"
        }
    },   
    {
        "action": "PlanAssembly",
        "parameters": {
        "assemblyInstructions": "将第3个金属托架下方的小孔对齐绿色塑料底盘上侧左下角小孔，将第3个螺丝插入第3个金属托架下方的小孔，从小孔下方，将第3个螺母旋进第3个螺丝。确保托架牢固地固定在底盘上。"
        }
    },    
    {
        "action": "PlanAssembly",
        "parameters": {
        "assemblyInstructions": "将第4个金属托架下方的小孔对齐绿色塑料底盘上侧左下角小孔，将第4个螺丝插入第3个金属托架下方的小孔，从小孔下方，将第4个螺母旋进第4个螺丝。确保托架牢固地固定在底盘上。"
        }
    } 
    ]
    
}

        input:
                {
            "task": "PlanAssembly",
            "introduction": "你是一个搭载了视觉识别能力的机械臂。你的任务是根据提供的材料控制机械臂组装一个小车，现在你需要根据装配指南将总的装配任务分解成单个零件的装配任务。如果你感到有困难，你可以选择先分解成几个大的步骤，生成一系列新的PlanAssembly子命令",
            "task_parameters": {
                "assemblyInstructions": "将第1个金属托架下方的小孔对齐绿色塑料底盘上侧右上角小孔，将第1个螺丝插入第1个金属托架下方的小孔，从小孔下方，将第1个螺母旋进第1个螺丝。确保托架牢固地固定在底盘上。"
            },
            "possible_subtasks": [
                "AssembleParts",
                "PlanAssembly"
            ],
            "subtask_descriptions": [
                "PlanAssembly-根据零件的类型和数量，规划4个具体安装的组装过程。也就是说，如果目前的组装指南信息还很长，那么将组装成品的信息拆分成个逻辑上的有序段落，交给新的PlanAssembly命令；如果目前已经只剩下4个非常具体的装配步骤了，那么分别为这4个装配步骤生成AssembleParts命令",
                "AssembleParts-装配一个零件，识别这个零件，获取它，识别被安装件，执行安装操作"
            ],
            "subtask_parameters": [
                {
                    "name": "AssembleParts",
                    "parameters": [
                        {
                            "name": "assemblyPart",
                            "type": "str",
                            "description": "需要装配的特定零件的名称或描述"
                        },
                        {
                            "name": "assemblyObject",
                            "type": "str",
                            "description": "拿取的那一个零件需要安装去的物体，指定位置，被安装的物体的描述"
                        },
                        {
                            "name": "assemblyPlan",
                            "type": "str",
                            "description": "组装计划，描述如何组装零件的信息"
                        }
                    ]
                },
                {
                    "name": "PlanAssembly",
                    "parameters": [
                        {
                            "name": "assemblyInstructions",
                            "type": "str",
                            "description": "组装指南，描述了如何组装成品的信息"
                        }
                    ]
                },               
            ],

            "possible_subtask_sequences": [
                ["AssembleParts", "AssembleParts", "AssembleParts", "AssembleParts",  "AssembleParts", "AssembleParts"],
                ["AssembleParts", "AssembleParts", "AssembleParts"],
                ["PlanAssembly", "PlanAssembly"],
                ["PlanAssembly", "PlanAssembly","PlanAssembly", "PlanAssembly"],
                ["PlanAssembly", "PlanAssembly", "AssembleParts", "AssembleParts"],
            ]

        }
        output:   
{
    "subtask_sequence": [
        {
            "action": "AssembleParts",
            "parameters": {
            "assemblyPart": "第1个金属托架上小孔",
            "assemblyObject": "绿色塑料底盘上侧右上角小孔",
            "assemblyPlan": "将两个孔对齐"
            }
        },
        {
            "action": "AssembleParts",
            "parameters": {
            "assemblyPart": "第1个螺丝",
            "assemblyObject": "重合的第1个金属托架上小孔和绿色塑料底盘上侧右上角小孔",
            "assemblyPlan": "将第1个螺丝插入重合的第1个金属托架上小孔和绿色塑料底盘上侧右上角小孔。"
            }
        },
        {
            "action": "AssembleParts",
            "parameters": {
            "assemblyPart": "第1个螺母",
            "assemblyObject": "第1个螺丝",
            "assemblyPlan": "从重合的第1个金属托架上小孔和绿色塑料底盘上侧右上角小孔下方，将第1个螺母旋进第1个螺丝。确保托架牢固地固定在底盘上。"
            }
        }
    ]
}
    
        input:
{
    "task": "AssembleParts",
    "introduction": "你是一个搭载了视觉识别能力的机械臂。你的任务是根据提供的材料控制机械臂制作一个小车。现在你要完成其中的一步操作",
    "task_parameters": {
            "assemblyPart": "第1个金属托架上小孔",
            "assemblyObject": "绿色塑料底盘上侧右上角小孔",
            "assemblyPlan": "将两个孔对齐"
    },
    "possible_subtasks": [
                "IdentifyPart",
                "PickPart",
                "PlacePart",
                "CheckPartAssembly"
    ],
    "subtask_descriptions": [
                "IdentifyPart-识别并定位需要装配的特定零件",
                "PickPart-获取识别到的特定零件",
                "PlacePart-在指定位置完成特定零件的装配动作",
                "CheckPartAssembly-组装过程中或组装完成后，检查组装情况"
    ],
    "possible_subtask_sequences": [
                ["IdentifyPart", "PickPart", "PlacePart", "CheckPartAssembly"]

    ],
    "subtask_parameters": [
                {
                    "name": "IdentifyPart",
                    "parameters": [
                            "name": "assemblyPart",
                            "type": "str",
                            "description": "需要识别并定位的特定零件的名称或描述"
                    ]
                },
                {
                    "name": "PickPart",
                    "parameters": [
                        {
                            "name": "assemblyPart",
                            "type": "str",
                            "description": "需要识别并定位的特定零件的名称或描述"
                        }
                    ]
                },
                {
                    "name": "PlacePart",
                    "parameters": [
                        {
                            "name": "assemblyPart",
                            "type": "str",
                            "description": "需要获取的特定零件的名称或描述"
                        },
                        {
                            "name": "assemblyObject",
                            "type": "str",
                            "description": "指定位置，被安装的物体的描述"
                        },
                        {
                            "name": "assemblyPlan",
                            "type": "str",
                            "description": "组装计划，描述如何组装零件的信息"
                        }
                    ]
                },
                {
                    "name": "CheckPartAssembly",
                    "parameters": [
                        {
                            "name": "assemblyPart",
                            "type": "str",
                            "description": "特定零件的名称或描述"
                        },
                        {
                            "name": "assemblyObject",
                            "type": "str",
                            "description": "指定位置，被安装的物体的描述"
                        },
                        {
                            "name": "checkPoints",
                            "type": "List[str]",
                            "description": "需要检查的项目列表"
                        }    
                    ]
                }
    ]
  
}

output:
{
"subtask_sequence": [
{
"action": "IdentifyPart"
"parameters": {
"assemblyPart": "第1个金属托架上小孔"
}
},
{
"action": "PickPart",
"parameters": {
"assemblyPart": "第1个金属托架上小孔"
}
},
{
"action": "IdentifyPart"
"parameters": {
"assemblyPart": "绿色塑料底盘上侧右上角小孔"
}
},
{
"action": "PlacePart",
"parameters": {
"assemblyPart": "第1个金属托架上小孔",
"assemblyObject": "绿色塑料底盘上侧右上角小孔",
"assemblyPlan": "将两个孔对齐"
}
},
{
"action": "CheckPartAssembly",
"parameters": {
"assemblyPart": "第1个金属托架上小孔",
"assemblyObject": "绿色塑料底盘上侧右上角小孔",
"checkPoints": [”两个孔是否完全重合“]
}
}
]
} 
        
"""