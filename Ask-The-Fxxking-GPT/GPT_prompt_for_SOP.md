

# GPTs for SOP

**润色论文的话，我的评价是谨慎，在不会修辞写作的情况下容易给GPT带飞**

他的写法非常的fancy， 很多古典形容词，建议修改成论文里别人用过的词

## Prompt Template

### Structure and reason:

1. Role
2. Main task
3. Input paragraphs 【一定要有title】
4. Repeat main task again
5. Notice
6. Format 

- 根据读的一些论文和实践表现，LLMs 会倾向于分析信息的前部和后部。
- 中间的段落不宜过长，一次一个subsection为佳
- 最好在subsection里有提前分好subsubsection，这样前后更有逻辑
- 对GPT 客气点（问好，赞叹）会有惊喜；也可以适当时候敲打，他可以被push 

## Custom Instruction

在找LLMs 精修SOP前，可以先设置一下你未来是做什么的，这样他的回答不至于偏的太离谱

- 你的专业能力（水平）
- 你了解的领域
- 你的project实现逻辑
- 你在投的论文/工作
- 你希望申请的专业

以我的为例：

1. What would you like ChatGPT to know about you to provide better responses?

> I am a senior student from the UIUC majoring in Computer Engineering. Standing at the intersection of human and machine interaction, my research interests include LLMs, Autonomous Driving and Computer Vision. I developed a project that integrates many advanced models, constructing a tool for LLMs, enabling them to understand road situations in textual form. As a result, the LLMs can act as a co-pilot, helping drivers assess the intentions of pedestrians. This helps identify potential risks on the road. Based on this project, I created an adaptive ARHUD risk warning system suitable for L3 automated driving scenarios. Now I am writing a personal statement for applying the graduate school in America.  

建议这个部分一定不要有语法错误，否则性能表现直线下降，可以找LLM帮你辅助查看

1. How would you like ChatGPT to respond?

> Provide expert advice that's deeply considered and tailored to my paper.
>
> 
>
> Be comprehensive and consise, while also inspiring a sense of action or deeper understanding.
>
> 
>
> At the end of each response, feel free to engage creatively in the conversation, pointing out the potential problem of current paper writing.

最有用的是最后一条，这样你询问任何问题，他都会给予关于文章的回复，有时候还挺inspiring的

接下来是各种短prompt，用于复制粘贴进行论文修改：

### Enhance

注意：""" 是不能删除的 ! 格式化输入有助于LLM理解

```Markdown
Act as a professional reviewer in Computer Science field and Human Computer Interaction. I have a paper named "XXX", to be submitted to Human Factors in Computing Systems (CHI). 
Here is a subsection of my paper, I need 
### subsection
"""
YOUR PARAGRAPHS
"""
I need you:
1. For each input paragraph, summarize into 50 words.
2. Based on your summary, enhance the subsection
```

这里可以考虑加COT， 或者直接：

```Markdown
Please enhance the following paragraphs without changing its main idea:
YOUR PARAGRAPHS
```

也可以：

```Markdown
Optimize these paragraphs without changing its main idea:
" PARAGRAPHS"
```

还有， 这的perspective 是你希望他注意的几个关键字，或者修辞学效果

> 1. 排比 (Parallelism)
>    1. 英文: Creating a balanced sentence by reusing the same word structure.
>    2. 中文: 通过重复相同的词结构来创建平衡的句子。
>    3. 示例: “The researcher must adequately equip, adequately prepare, and adequately execute the experiment.”
> 2. 类比 (Analogy)
>    1. 英文: Making a comparison between two things to explain a concept more clearly.
>    2. 中文: 比较两者来更清楚地解释一个概念。
>    3. 示例: “The neurons in a neural network operate in a fashion akin to the synapses in a human brain.”
> 3. 排除法 (Process of Elimination)
>    1. 英文: Explicitly noting what your work does not encompass can help to sharpen the focus on what it does encompass.
>    2. 中文: 明确指出您的工作不包含什么可以帮助更加清晰地聚焦于它所包含的内容。
>    3. 示例: “While our research touches upon the broader implications of machine learning, it distinctly avoids a deep dive into neural networks.”
> 4. 疑问句 (Rhetorical Question)
>    1. 英文: Asking a question to which no answer is required, typically to illustrate a clear or obvious point.
>    2. 中文: 提出一个不需要答案的问题，通常是为了说明一个清晰或明显的观点。
>    3. 示例: “Are we to ignore the promising results yielded by preliminary studies?”
> 5. 前后呼应 (Epistrophe)
>    1. 英文: The repetition of a word or phrase at the end of successive clauses to emphasize a point through repetition.
>    2. 中文: 在连续子句的末尾重复一个词或短语，通过重复来强调一个点。
>    3. 示例: “The system enhanced safety, the system enhanced efficiency, the system enhanced reliability.”
> 6. 对比 (Contrast)
>    1. 英文: Highlighting the difference between two elements to underscore a key point.
>    2. 中文: 强调两个元素之间的差异来突出一个关键点。
>    3. 示例: “Unlike conventional methods, our algorithm allows for real-time, on-the-fly adjustments.”

```Markdown
Enhance this paragraphs from XXX perspectives：
```

也可以试试：

```Markdown
### Abstract
你的abstract

Based on the given abstract, please enhance the following paragraphs without changing its main idea:
"""
YOUR PARAGRAPHS
"""
```

### Translation

这个prompt是辅助大家在使用中文梳理逻辑后，用GPT帮忙输出一个初稿所用。

- 注意这里可以加role也可以不用加，经过测试，简单祈使句的翻译效果可能会更通用
- markdown输出往往会有更好更稳定的表现
- latex输出往往会扭曲一部分内容（可能和训练语料有关）

```SQL
Translate this into English without changing its main idea:
"""
YOUR PARAGRAPHS
"""
Your translation should be professional and academic but also plain for everyone to understand.
Your response should be in markdown
```

可选：

指定一些 翻译术语列表，例如：

```Markdown
You can use this list to help your translation:
"""
Scene understanding: 场景理解
Yield: 让步/让路
Take the right of way: 辨别方位
Cross the street / Jaywalk / Crossing: 横穿马路
"""
```

### Grammar Check( best practice)

```Markdown
Help me check if there is grammmar error in the following paragraphs:
```

一般这时候，聪明的GPT4就应该用Markdown输出很多好建议了

你也可以试试用他检查逻辑

### Logic Check（一般用ENHANCE ）

```Markdown
Check if there is logic error in the in the following paragraphs:
"""
YOUR PARAGRAPHS
"""
You can:
1. think step by step
2. summary the paragraphs
3. critically reply as a professor in XXX field
```

这里可以随意更改这个123， 用这种输入方式可以加强LLM的理解能力

## 最后：

不要直接使用LLM的输出，相信他是在瞎写，虽然看似很对，但有很多需要check的细节

之后需要把他乱七八糟的词去掉, 换成正常人懂的, 还有就是各种长短句压缩改写

其实可以限制他用词水平, 比方说让他的陈述academic and intuitive  OR 

plain but concise

总之多调试，点一下regenerate, 一般还行

### Rhetorical Writing : 长短相随，变化有致、

长短句，同一个表述变化，保持客观

一般没问题

更高级的ETHOS, LOGOS, PATHOS...