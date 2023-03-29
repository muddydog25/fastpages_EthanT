---
keywords: fastai
title: Unit 3 Sections 17-18 Hacks
badges: true
comments: true
author: Ethan Tran
categories: [unit 3, sections 17-18, hacks]
nb_path: _notebooks/2022-12-15-Unit-3-Sections-17-18-Hacks.ipynb
layout: notebook
---

<!--
#################################################
### THIS FILE WAS AUTOGENERATED! DO NOT EDIT! ###
#################################################
# file to edit: _notebooks/2022-12-15-Unit-3-Sections-17-18-Hacks.ipynb
-->

<div class="container" id="notebook-container">
        
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Notes-(From-the-lesson-+-extra-research)">Notes (From the lesson + extra research)<a class="anchor-link" href="#Notes-(From-the-lesson-+-extra-research)"> </a></h2><ul>
<li>The Collatz Conjecture is an unsolved problem in mathematics that involves repeating two simple arithmetic operations on any given positive integer. This will eventually produce a sequence of numbers known as Hailstone Numbers, </li>
</ul>
<p><strong>Example:</strong> If the input is 7, the Hailstone Numbers would be 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1. Iteration is the action or process of repeating a sequence of operations until the desired result is achieved. Undecidable problems are those which should give a yes or no answer, yet no algorithm exists that can answer correctly on all inputs.</p>
<ul>
<li><p>Algorithm efficiency in computer science refers to how efficient an algorithm is at solving a given problem.</p>
</li>
<li><p>Efficiency is typically measured in terms of time and/or space complexity, meaning how much time and/or memory is needed to complete the algorithm. Algorithm efficiency is an important factor in determining which algorithm should be used to solve a particular problem.</p>
</li>
</ul>
<ol>
<li><p>Time Complexity: This measures the amount of time required to execute an algorithm. Time complexity is usually expressed as a function of the input size, and can be calculated using Big-O notation. Generally, algorithms with a lower time complexity are considered more efficient than those with a higher time complexity.</p>
</li>
<li><p>Space Complexity: This measures the amount of memory required to execute an algorithm. Space complexity is also expressed as a function of the input size, and can also be calculated using Big-O notation. Generally, algorithms with a lower space complexity are considered more efficient than those with a higher space complexity.</p>
</li>
<li><p>Optimization Techniques: Optimization techniques can be used to improve the efficiency of an algorithm. These techniques can involve modifying the algorithm itself, or using data structures and algorithms that are better suited to the problem.</p>
</li>
<li><p>Parallelism: Parallelism is a technique that allows multiple parts of an algorithm to be executed simultaneously. This can significantly reduce the amount of time required to complete the algorithm, but can also increase the complexity of the algorithm.</p>
</li>
</ol>
<p><strong>In conclusion,</strong> algorithm efficiency is an important factor in determining which algorithm should be used to solve a particular problem. Factors such as time complexity, space complexity, optimization techniques, and parallelism should all be taken into consideration when assessing the efficiency of an algorithm.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Hack-#1">Hack #1<a class="anchor-link" href="#Hack-#1"> </a></h3><ul>
<li>Take the two codes above and combine them so one imput gives the output that contains both the hailstone numbers and the number of iterations it takes i = 1. (.25)</li>
</ul>
<p>(Extra credit: If your code is more efficient it will recieve a higher grade.)</p>

</div>
</div>
</div>
    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">i</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="nb">input</span><span class="p">(</span><span class="s2">&quot;Please input a number: &quot;</span><span class="p">))</span>
<span class="nb">list</span> <span class="o">=</span> <span class="p">[]</span>

<span class="k">def</span> <span class="nf">collatz_seq</span><span class="p">(</span><span class="n">n</span><span class="p">):</span>
    <span class="nb">list</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">while</span> <span class="n">n</span> <span class="o">!=</span> <span class="mi">1</span><span class="p">:</span>
        <span class="k">if</span> <span class="p">(</span><span class="n">n</span> <span class="o">%</span> <span class="mi">2</span><span class="p">):</span>
            <span class="n">n</span> <span class="o">=</span> <span class="mi">3</span><span class="o">*</span><span class="n">n</span> <span class="o">+</span> <span class="mi">1</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">n</span> <span class="o">=</span> <span class="n">n</span><span class="o">/</span><span class="mi">2</span>
        <span class="nb">list</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">n</span><span class="p">)</span>
    <span class="k">return</span> <span class="nb">list</span>

<span class="n">result</span> <span class="o">=</span> <span class="n">collatz_seq</span><span class="p">(</span><span class="n">i</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Input:&quot;</span> <span class="p">,</span> <span class="n">i</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Iteration count:&quot;</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">result</span><span class="p">))</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">

<div class="output_subarea output_stream output_stdout output_text">
<pre>Input: 77
[232, 116.0, 58.0, 29.0, 88.0, 44.0, 22.0, 11.0, 34.0, 17.0, 52.0, 26.0, 13.0, 40.0, 20.0, 10.0, 5.0, 16.0, 8.0, 4.0, 2.0, 1.0]
Iteration count: 22
</pre>
</div>
</div>

</div>
</div>

</div>
    {% endraw %}

<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Hack-#2">Hack #2<a class="anchor-link" href="#Hack-#2"> </a></h3><p>1) Code 2 algorithms: (.25)</p>
<p>The first Algorithm should be efficient while the second should be inefficient. Then explain what distinguishes the efficient from the non-efficient one. (In your own words)</p>

</div>
</div>
</div>
    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">car</span> <span class="o">=</span> <span class="p">[]</span>

<span class="n">car</span><span class="o">.</span><span class="n">append</span><span class="p">({</span>
    <span class="s2">&quot;Make&quot;</span><span class="p">:</span> <span class="s2">&quot;BMW&quot;</span><span class="p">,</span>
    <span class="s2">&quot;Model&quot;</span><span class="p">:</span> <span class="s2">&quot;M4 CSL&quot;</span><span class="p">,</span>
    <span class="s2">&quot;Year&quot;</span><span class="p">:</span> <span class="s2">&quot;2023&quot;</span><span class="p">,</span>
<span class="p">})</span>
<span class="k">def</span> <span class="nf">loop</span><span class="p">():</span>
    <span class="k">for</span> <span class="n">data</span> <span class="ow">in</span> <span class="n">car</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>

<span class="n">loop</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">

<div class="output_subarea output_stream output_stdout output_text">
<pre>{&#39;Make&#39;: &#39;BMW&#39;, &#39;Model&#39;: &#39;M4 CSL&#39;, &#39;Year&#39;: &#39;2023&#39;}
</pre>
</div>
</div>

</div>
</div>

</div>
    {% endraw %}

    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">car</span> <span class="o">=</span> <span class="s2">&quot;Make: BMW&quot;</span><span class="p">,</span> <span class="s2">&quot;Model: M4 CSL&quot;</span><span class="p">,</span> <span class="s2">&quot;Year: 2023&quot;</span>
<span class="nb">print</span><span class="p">(</span><span class="n">car</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">

<div class="output_subarea output_stream output_stdout output_text">
<pre>(&#39;Make: BMW&#39;, &#39;Model: M4 CSL&#39;, &#39;Year: 2023&#39;)
</pre>
</div>
</div>

</div>
</div>

</div>
    {% endraw %}

<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Algorithm 1 properly displays efficiency, as it appends the list and utilizes a for loop in order to display the data of the given car in an orderly manner. Algorithm 2 is inefficient because the data is only displayed in the order that it is typed in.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<ul>
<li>Explain algorithm efficiency in your own words (.25)</li>
</ul>
<p>Algorithm efficiency in computer science is the measure of how well a particular algorithm performs when compared to other algorithms. It is typically calculated by measuring the amount of time and space it takes to complete a task. The most efficient algorithms are those that take the least amount of time to complete a task while consuming the smallest amount of resources. In other words, the most efficient algorithms are those that are able to accomplish a task in the shortest amount of time with the least amount of memory and CPU cycles.</p>
<ul>
<li>Code an efficient program that shows your daily tasks or schedule. (We have an example shown in our lesson) (.25)</li>
</ul>

</div>
</div>
</div>
    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">tasks</span> <span class="o">=</span> <span class="p">[</span><span class="s2">&quot;wake up&quot;</span><span class="p">,</span> <span class="s2">&quot;get ready&quot;</span><span class="p">,</span> <span class="s2">&quot;head to school&quot;</span><span class="p">,</span> <span class="s2">&quot;finish homework/study&quot;</span><span class="p">,</span> <span class="s2">&quot;go to bed&quot;</span><span class="p">]</span>
 
<span class="k">def</span> <span class="nf">daily_routine</span><span class="p">(</span><span class="n">tasks</span><span class="p">):</span>
 <span class="k">for</span> <span class="n">task</span> <span class="ow">in</span> <span class="n">tasks</span><span class="p">:</span>
 
    <span class="k">if</span> <span class="n">task</span> <span class="o">==</span> <span class="s2">&quot;wake up&quot;</span><span class="p">:</span>
     <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Waking up!&quot;</span><span class="p">)</span>
    <span class="k">elif</span> <span class="n">task</span> <span class="o">==</span> <span class="s2">&quot;get ready&quot;</span><span class="p">:</span>
     <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Getting ready!&quot;</span><span class="p">)</span>
    <span class="k">elif</span> <span class="n">task</span> <span class="o">==</span> <span class="s2">&quot;head to school&quot;</span><span class="p">:</span>
       <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Heading to school!&quot;</span><span class="p">)</span>
    <span class="k">elif</span> <span class="n">task</span> <span class="o">==</span> <span class="s2">&quot;finish homework/study&quot;</span><span class="p">:</span>
       <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Working hard!&quot;</span><span class="p">)</span>
    <span class="k">elif</span> <span class="n">task</span> <span class="o">==</span> <span class="s2">&quot;going to bed&quot;</span><span class="p">:</span>
       <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Time for bed!&quot;</span><span class="p">)</span>

<span class="n">daily_routine</span><span class="p">(</span><span class="n">tasks</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">

<div class="output_subarea output_stream output_stdout output_text">
<pre>Waking up!
Getting ready!
Heading to school!
Working hard!
</pre>
</div>
</div>

</div>
</div>

</div>
    {% endraw %}

    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">getpass</span> <span class="kn">import</span> <span class="n">getpass</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">

<div class="output_subarea output_text output_error">
<pre>
<span class="ansi-cyan-intense-fg ansi-bold">  File </span><span class="ansi-green-intense-fg ansi-bold">&lt;tokenize&gt;:26</span>
<span class="ansi-yellow-intense-fg ansi-bold">    else:</span>
<span class="ansi-white-intense-fg ansi-bold">    ^</span>
<span class="ansi-red-intense-fg ansi-bold">IndentationError</span><span class="ansi-red-intense-fg ansi-bold">:</span> unindent does not match any outer indentation level
</pre>
</div>
</div>

</div>
</div>

</div>
    {% endraw %}

</div>
 
