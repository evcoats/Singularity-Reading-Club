# Self-Improving Systems: A Historical & Conceptual Primer for Scalable Oversight
### A 90-minute hybrid graduate seminar — University of Illinois Urbana-Champaign

> **Verification note (read first).** The automated web tools in the authoring environment were non-operational, so every quotation below is drawn from well-established primary works and is tagged with a confidence level: **[VERBATIM — high confidence]**, **[SUBSTANCE confident, wording verify]**, or **[PARAPHRASE — reconstruct before quoting on a slide]**. Bibliographic facts (authors, titles, years, journals, volumes, pages) are high-confidence. **URLs are given in their canonical form but were NOT liveness-tested; test each before the session and do not project a link you have not opened yourself.** Where a popular attribution is disputed, that is flagged inline. This honesty is itself a teaching point: a primer about oversight should model verifiable sourcing.

---

## TL;DR
1. **The through-line is one idea seen four ways.** Von Neumann's automata show *self-reproduction* (copy a description without changing it); Gödel numbering and neuroplasticity show *self-reference* and *self-modification* (a system encodes and rewrites itself); fractals/recursion show *scale* (structure and difficulty that may or may not look the same at every magnification). Scalable oversight — supervising systems on tasks we cannot directly judge, especially as they grow more capable than us — is exactly the problem of controlling systems that reference, modify, reproduce, and scale themselves.
2. **The historical figures already stated the oversight problem in their own terms.** I.J. Good's 1965 "intelligence explosion," Turing's 1951 "we should have to expect the machines to take control," and Sagan & Newman's 1983 warning that a self-replicating probe could become an uncontrollable galaxy-consuming plague are all pre-1985 statements of the "capable, self-propagating system we cannot recall" problem. This lets the seminar discuss oversight rigorously **without touching any current alignment method.**
3. **The deepest single insight for the room is von Neumann's genotype/phenotype split** — a description is read *twice*, once as instructions (interpreted/executed) and once as data (copied verbatim, uninterpreted) — which anticipated the logic of DNA before Watson–Crick (1953) and which reframes the oversight question: *is the separation of "copy" from "interpret" a lever we could use to supervise a self-propagating system?*

---

## FRAMING: The problem of scalable oversight (≈10 min, opening slides)

**State the problem plainly.** Scalable oversight is the problem of *supervising and evaluating an AI system on tasks where humans cannot cheaply or reliably judge the outputs* — and this only gets harder as systems approach or exceed the competence of their overseers, and harder still when the system can improve, modify, or reproduce itself faster than we can inspect it.

**Citable problem statement.** Dario Amodei, Chris Olah, Jacob Steinhardt, Paul Christiano, John Schulman, and Dan Mané, *Concrete Problems in AI Safety* (2016), arXiv:1606.06565 — treat scalable oversight as one of five concrete problems: the challenge of ensuring an agent "respects aspects of the objective that are too expensive to be evaluated frequently during training," i.e., behaving well even in situations the designer can only rarely observe. **[SUBSTANCE confident; verify the exact one-sentence definition against §"Scalable Oversight" in the PDF.]** URL: `https://arxiv.org/abs/1606.06565`.

**Why these three historical blocks are the right lenses (say this out loud at the start):**
- **Self-reproduction (Block 1):** Once a system copies itself and leaves, oversight must survive replication and distance. Von Neumann gives the cleanest logical anatomy of self-reproduction; Dyson gives the "you cannot recall it" version.
- **Self-reference & self-modification (Block 2):** A system that encodes a description of itself (Gödel) or rewrites its own update rule (metaplasticity, learned optimizers) is harder to predict and to certify than one with a fixed rule. Gödel also gives a *limit* result: a system can talk about itself but cannot fully certify itself.
- **Scale (Block 3):** Oversight's central worry is capability that outruns the overseer. Self-similarity forces the precise question: *does the difficulty of supervision look the same at every scale (self-similar), or are there phase transitions?*

**Ground rule for the room (put on a slide):** *No current methods.* We will not discuss debate, amplification, recursive reward modeling, weak-to-strong generalization, RLHF, etc. This is a history-and-concepts session; the payoff is sharper intuitions, not a toolbox.

---

# BLOCK 1 — John von Neumann's self-reproducing automata + Freeman Dyson's Astrochicken (30 min)

**Suggested timing:** 5 min biography · 12 min universal constructor + DNA parallel + complexity threshold · 6 min Astrochicken & von Neumann probes · 7 min discussion.

### 1a. Biography (5 min)

**John von Neumann (1903–1957).** Born Neumann János Lajos in **Budapest** in 1903 into a prosperous Jewish family (his father, a banker, was ennobled, giving the "von"/"Margittai"). A prodigy — reportedly able to divide eight-digit numbers in his head as a child and to converse in Ancient Greek. He earned a chemical-engineering diploma in Zürich and a mathematics doctorate in Budapest almost simultaneously (1926). He moved to Princeton in 1930 and became one of the founding professors of the **Institute for Advanced Study (IAS)** in 1933. His fingerprints are on: the mathematical foundations of quantum mechanics (1932), the **minimax theorem and game theory** (1928; *Theory of Games and Economic Behavior* with Morgenstern, 1944), the **Manhattan Project** (implosion-lens design at Los Alamos), and the **stored-program computer architecture** described in the *First Draft of a Report on the EDVAC* (1945) — the reason we say "von Neumann architecture." He gave the **University of Illinois lectures in December 1949**, and died of cancer in Washington, D.C., on **February 8, 1957**.

*Local UIUC hook (make this explicit):* the December 1949 lectures that seeded *Theory of Self-Reproducing Automata* were delivered at the **University of Illinois**, and the completing editor, **Arthur W. Burks**, was closely tied to Illinois-adjacent computing history (ENIAC, and later the University of Michigan). The book was published by the **University of Illinois Press (1966)**. This is a genuinely local origin story for the theory of self-reproduction.

**Freeman Dyson (1923–2020).** English-born mathematical physicist. Studied at **Cambridge**, moved to **Cornell** and then to the **IAS at Princeton** (where he overlapped with von Neumann). His famous early achievement was showing the **equivalence of the Feynman, Schwinger, and Tomonaga formulations of quantum electrodynamics (QED)** (1949) — arguably the work that "should" have won him a share of a Nobel. He never took a PhD. Later he worked on **Project Orion** (nuclear-pulse propulsion), proposed the **Dyson sphere** (1960, *Science*, "Search for Artificial Stellar Sources of Infrared Radiation"), and wrote widely read essays. He died on **February 28, 2020**.

**The personal/anecdotal von Neumann–Dyson connection.** Both were IAS members; Dyson knew von Neumann personally at Princeton. Dyson's memoir *Disturbing the Universe* (1979) recounts von Neumann at the IAS and is famously ambivalent about von Neumann's computing project and his personality. A frequently retold anecdote: Dyson recalled von Neumann's dismissiveness toward using the IAS computer for "unimportant" problems like weather/astrophysics that Dyson cared about. **[SUBSTANCE confident; the specific phrasing should be quoted directly from *Disturbing the Universe* — verify the exact page before putting a quotation on a slide.]** The clean, defensible statement for a slide: *Dyson and von Neumann were IAS contemporaries; Dyson wrote about von Neumann's computer project critically in* Disturbing the Universe.

### 1b. The precursor and the lectures (part of the 12-min block)

- **1948 Hixon Symposium:** von Neumann's lecture **"The General and Logical Theory of Automata,"** delivered at the Hixon Symposium (Caltech, September 1948), published in *Cerebral Mechanisms in Behavior: The Hixon Symposium*, ed. L.A. Jeffress (Wiley, 1951), pp. 1–41. This is where he first laid out the automata program and the complexity-threshold argument.
- **December 1949 Illinois lectures:** "Theory and Organization of Complicated Automata" — five lectures at the University of Illinois. Von Neumann intended a large treatise but never finished it.
- **Burks's reconstruction:** After von Neumann's 1957 death, **Arthur W. Burks** edited and completed the material, publishing *Theory of Self-Reproducing Automata* (University of Illinois Press, 1966). Burks reconstructed the unfinished cellular-automaton (Part II) work from von Neumann's manuscripts and added extensive editorial commentary. Point out to the room: *the canonical text of the theory of self-reproduction is itself a reconstruction — a description completed by a second author*, which is a nice meta-joke given the subject. Likely archive.org copy (test first): search `Theory of Self-Reproducing Automata von Neumann` at `https://archive.org/`.

### 1c. The universal constructor (core of the block)

Von Neumann asked: *can a machine build a machine as complex as itself — including itself?* His logical answer separates the machine into functional parts plus a description:

- **A — the universal constructor:** given a description (tape) φ(X) of any machine X, A builds X.
- **B — the copier:** given a tape, B produces an identical copy of the tape. **Crucially, B copies the tape verbatim, without interpreting it.**
- **C — the controller:** orchestrates A and B — first have A build the machine from the description, then have B copy the description, then attach the copied description to the new machine, then release.
- **φ(A + B + C) — the description/tape:** an encoded blueprint of the whole ensemble.

The complete self-reproducing automaton is **(A + B + C) + φ(A + B + C)**. Fed its own description, it builds a copy of A+B+C (via A), copies the description (via B), and hands the copy its own description — producing a full, independent copy of itself, description included. This is the logical resolution of the apparent paradox ("must the blueprint contain a blueprint of the blueprint of the blueprint…?"): **the description is used twice — once interpreted as instructions (A reads it as *what to build*), once un-interpreted as data (B copies it as *raw symbols*).** That dual use breaks the infinite regress.

**Two models von Neumann developed:**
1. **The kinematic model** — machines floating in a "sea" of spare parts (girders, sensors, motors, logic elements), assembling copies mechanically. Intuitive but physically messy.
2. **The 29-state cellular automaton (CA) model** — a 2D grid where each cell takes one of **29 states**, updated by a fixed local rule. This is the rigorous, fully-specified version (completed by Burks), in which a configuration of cells constitutes the constructor and the tape is a line of cells encoding the description. This is what Golly ships.

**The key oversight-relevant property: the reproduction mechanism is NOT modified during replication.** The copier B copies the tape *verbatim*; A, B, C are rebuilt identically. Nothing in the machine "improves" itself — it *reproduces*. Improvement requires something else (see 1e).

### 1d. The DNA parallel (part of the 12-min block)

Von Neumann's genotype/phenotype split anticipated molecular biology. In cells:
- The **description read as data** ↔ **DNA replication** (the double helix is copied base-by-base, without interpreting what the genes "mean").
- The **description read as instructions** ↔ **transcription/translation** (genes are interpreted to build proteins — the phenotype).

This maps precisely onto B (copy without interpreting) vs. A (interpret to construct). Von Neumann described this *before* Watson & Crick's **1953** double-helix structure and before the articulation of the central dogma. Emphasize: this is a case of the *logical* requirements of self-reproduction predicting the *biological* solution.

**Sydney Brenner's remarks.** Brenner (Nobel 2002; co-decipherer of the triplet genetic code) repeatedly credited von Neumann with anticipating the logic of the genetic code — that a self-reproducing system needs a description used in two ways, as instructions to be executed and as data to be copied. **[PARAPHRASE — reconstruct verbatim before quoting.]** Reconstructed sense: *"von Neumann showed that a self-reproducing machine needs a description of itself that it uses in two ways — as instructions to be executed and as data to be copied — and this was exactly what was needed for the genetic material."* Source to verify: Sydney Brenner, *My Life in Science* (as told to Lewis Wolpert; eds. Friedberg & Lawrence, BioMed Central, 2001), and his **Web of Stories** video interviews (`https://www.webofstories.com/play/sydney.brenner`). **Flag to the room that the wording is unverified.**

**Von Neumann's own statement of the instructions/data duality** should be quoted from Burks (1966) directly; I do not have it verbatim with high confidence, so **reconstruct it from the primary text rather than trusting memory.**

### 1e. The complexity threshold and the mutation/evolution point

Von Neumann's most self-improvement-relevant argument (from the 1948 Hixon lecture and elaborated in the 1966 book): there is a **critical level of complexity**. *Below* it, synthesis is **degenerative** — a machine can only build things simpler than itself, so complexity dies out. *Above* it, the process can be **self-sustaining or explosive** — a machine can build machines of *equal or greater* complexity than itself. **[PARAPHRASE — the exact sentence must be pulled from the Hixon text / Burks 1966; do not quote my wording verbatim.]** Reconstructed sense: *"There is a minimum number of parts below which complication is degenerative… but above which it is possible for an automaton to construct others of equal or higher complexity."*

**The evolution hook:** von Neumann noted that if a **mutation** occurs in the *description* (the tape), that change is **inherited** — copied by B into the offspring's description — which makes **evolution** possible. This is the precise conceptual bridge from mere *self-reproduction* to potential *self-improvement*: reproduction + heritable variation + selection = evolution. Pure verbatim copying alone is **not** self-improvement.

### 1f. Later implementations & interactive visuals (mention while showing)

- **Renato Nobili & Umberto Pesavento (1995):** the first full working implementation of von Neumann's self-reproducing constructor in the 29-state CA. Key paper: **U. Pesavento, "An Implementation of von Neumann's Self-Reproducing Machine," *Artificial Life* 2(4), 1995, pp. 337–354 (MIT Press)** (with an introduction by Nobili). Verify at `https://direct.mit.edu/artl` (search the title).
- **Golly** — the open-source CA simulator (`https://golly.sourceforge.net/`). It ships **von Neumann's 29-state rule** and includes **Nobili–Pesavento self-replicator patterns** in its supplied pattern library. A web build exists (`https://golly.sourceforge.net/webapp/golly.html` — **test liveness**). *On screen:* load the von Neumann rule, open the self-rep pattern, and step it so students watch the constructor arm build a copy and the tape get copied.
- **Tim Hutton** — corrected/completed von Neumann-style constructors and built fully self-reproducing configurations; also author of "Codd's Self-Replicating Computer" (*Artificial Life*, 2010) and maintainer of the **Ready** reaction-diffusion project. GitHub: `https://github.com/timhutton`.
- **William R. Buckley** — published work on von Neumann self-replicator design and signal-crossing solutions in the 29-state CA (search Buckley + *Artificial Life* / *Complex Systems*).
- **Video:** search YouTube for `von Neumann universal constructor Golly` / `Nobili Pesavento self-replicating` — several screen-captures of the constructor running exist. **Pick one and pre-load it; I could not confirm a specific video ID.**

### 1g. Freeman Dyson's Astrochicken + von Neumann probes (6 min)

**Astrochicken.** In *Infinite in All Directions* (Harper & Row, 1988; based on his **Gifford Lectures**), Dyson proposed the "Astrochicken": a spacecraft **"about one kilogram in weight"** — a self-reproducing, self-growing probe *grown from a genetically engineered seed/egg*, combining **biological components** (genetic engineering — for the body, energy harvesting, self-repair) with **electronic/AI components** (for navigation and decision-making), solar-powered, able to explore the outer solar system and reproduce using local materials. **[Mass "about one kilogram" — SUBSTANCE confident; the surrounding descriptive phrasing is PARAPHRASE — verify against the 1988 text.]** He had floated self-reproducing machines earlier in ***Disturbing the Universe* (1979)** and in a 1970 vision of space colonization. *On screen:* read the "one kilogram / grown from an egg" passage and ask what "supervising" it would even mean once launched.

**Von Neumann probes and the oversight/ETI debate:**
- **Ronald Bracewell (1960):** proposed autonomous interstellar messenger probes ("Bracewell probes") as an alternative to radio SETI.
- **Frank J. Tipler (1980), "Extraterrestrial Intelligent Beings Do Not Exist,"** *Quarterly Journal of the Royal Astronomical Society* 21, pp. 267–281: argued that any advanced civilization would eventually build **self-replicating von Neumann probes** ("universal constructors") that could colonize the entire Galaxy on cosmically short timescales; since we see none, *we are probably alone.* ADS: `https://ui.adsabs.harvard.edu/abs/1980QJRAS..21..267T` (**verify bibcode**).
- **Carl Sagan & William I. Newman (1983), "The Solipsist Approach to Extraterrestrial Intelligence,"** *QJRAS* 24, pp. 113–121: **rebuttal.** They argued self-replicating probes are **too dangerous to build** — a design flaw or mutation could turn them into a runaway, resource-consuming plague that devours the very civilization that launched it (and everything else). A wise civilization would therefore refrain, so their absence does **not** prove ETI's absence. **[SUBSTANCE confident; wording PARAPHRASE — verify.]** ADS: `https://ui.adsabs.harvard.edu/abs/1983QJRAS..24..113S` (**verify bibcode**).
- **"Berserkers":** Fred Saberhagen's SF concept (1960s) of self-replicating machines that destroy life — the cultural shorthand for hostile runaway replicators, useful as the vivid version of the Sagan–Newman worry.

**The oversight hook (say it explicitly):** Sagan & Newman's 1983 concern — *a self-replicating system that cannot be recalled and may mutate into something uncontrollable* — is a 1983 statement of the scalable-oversight worry in astronomical dress.

### 1h. Block 1 discussion points (for slides)
1. Von Neumann *separates* the thing that copies (B) from the thing that builds (A) and from the description (φ). **Is that separation a lever for oversight** — e.g., could you supervise the "copy" channel independently of the "interpret" channel?
2. A system that copies its description **verbatim** is *self-reproducing* but arguably not *self-improving*. **What, exactly, turns reproduction into improvement?** (Answer to elicit: heritable variation + selection — i.e., mutation in the tape.)
3. Mutations in the description are inherited. **Does that make the constructor safer or more dangerous to oversee?**
4. **What would oversight of an Astrochicken or a von Neumann probe even look like once it has left** and is beyond communication latency and recall?

---

# BLOCK 2 — Gödel numbering + neuroplasticity (30 min)

**Suggested timing:** 8 min Gödel/self-reference + the self-modifying-machines lineage · 10 min neuroplasticity history · 8 min the bridge (honest analysis) · 4 min discussion.

### 2a. Gödel numbering and self-reference (part of the 8-min block)

**Gödel 1931.** Kurt Gödel, *"On Formally Undecidable Propositions of Principia Mathematica and Related Systems I"* (*Über formal unentscheidbare Sätze…*, 1931). The core technical device is **Gödel numbering**: assign a unique natural number to every symbol, formula, and proof, so that statements *about* the formal system (e.g., "formula X is provable") become statements *about numbers* — expressible *inside* the system. This lets a system **talk about itself.** The **diagonal (fixed-point) lemma** then constructs a sentence G that effectively asserts *"G is not provable in this system."* If the system is consistent, G is true but unprovable → **incompleteness.** English translation: van Heijenoort (ed.), *From Frege to Gödel: A Source Book in Mathematical Logic, 1879–1931* (Harvard, 1967), pp. 596–616; alternative Meltzer translation circulates on archive.org. **Quote the opening ("The development of mathematics toward greater precision has led… to the formalization of large tracts of it…") only after checking which translation you are using — [SUBSTANCE confident, wording varies by translator].** Good secondary anchor: Stanford Encyclopedia of Philosophy, "Gödel's Incompleteness Theorems," `https://plato.stanford.edu/entries/goedel-incompleteness/`.

**The computational analogs.**
- **Kleene's recursion theorem:** any computable transformation of programs has a fixed point — concretely, **a program can obtain its own source code** and use it. This is the computability-theory sibling of the diagonal lemma.
- **Quines:** programs that print their own source. A quine is the executable, minimal demonstration of the *instructions-and-data* duality: the source is both *run* (instructions) and *reproduced* (data) — **exactly von Neumann's φ read two ways.**
- **The bridge to Block 1:** von Neumann's description tape is a *Gödel-numbering-like encoding of the machine*; copying the tape is the "data" reading, constructing from it is the "instruction" reading. Scholars who explicitly connect self-reproduction to Gödel/Kleene include **Hofstadter** (*GEB* discusses self-rep, quines, and the recursion theorem together) and treatments in recursion-theory texts (e.g., Hartley Rogers). *Discussion seed:* self-reproduction, quines, and the Gödel sentence are three faces of one fixed-point construction.

**Hofstadter on strange loops.** Douglas Hofstadter, *Gödel, Escher, Bach: An Eternal Golden Braid* (Basic Books, 1979). **[VERBATIM — high confidence; verify page]:** *"My belief is that the explanations of 'emergent' phenomena in our brains — for instance, ideas, hopes, images, analogies, and finally consciousness and free will — are based on a kind of Strange Loop, an interaction between levels in which the top level reaches back down towards the bottom level and influences it, while at the same time being itself determined by the bottom level."* Archive.org likely hosts a scan (test first).

### 2b. The self-modifying-machines lineage (historical only — part of the 8-min block)

- **Turing 1950**, *"Computing Machinery and Intelligence,"* *Mind* 59(236) — the section on **learning machines** (the "child machine" that is educated rather than programmed). URL: `https://doi.org/10.1093/mind/LIX.236.433`.
- **Turing 1951 lecture, "Intelligent Machinery, A Heretical Theory"** (to the '51 Society, Manchester; published posthumously — e.g., in *The Essential Turing*, ed. Copeland, 2004). **[VERBATIM — high confidence; verify exact wording against the Turing Digital Archive, ref. AMT/B/4, `https://turingarchive.kings.cam.ac.uk/`]:** *"…once the machine thinking method had started, it would not take long to outstrip our feeble powers… At some stage therefore we should have to expect the machines to take control, in the way that is mentioned in Samuel Butler's 'Erewhon.'"* **Dispute flag:** the popular one-line version ("they would be able to converse with each other to sharpen their wits") is often quoted; treat the exact sentence-by-sentence wording as needing verification against the manuscript, because paraphrases circulate widely.
- **I.J. Good 1965, "Speculations Concerning the First Ultraintelligent Machine,"** *Advances in Computers* 6, pp. 31–88. **[VERBATIM — high confidence]:** *"Let an ultraintelligent machine be defined as a machine that can far surpass all the intellectual activities of any man however clever. Since the design of machines is one of these intellectual activities, an ultraintelligent machine could design even better machines; there would then unquestionably be an 'intelligence explosion,' and the intelligence of man would be left far behind. Thus the first ultraintelligent machine is the last invention that man need ever make, provided that the machine is docile enough to tell us how to keep it under control."* This is the canonical historical statement of recursive self-improvement *and* the oversight caveat ("docile enough… to keep it under control"). PDFs circulate; verify a stable host.
- **Löb's theorem (1955), informal, historical only:** a sufficiently strong consistent system cannot prove "if this sentence is provable, it is true" for arbitrary sentences — informally, a formal system **cannot simply trust a blanket assertion of its own (or a successor's) soundness.** Present *only* as the logical shadow of "a system cannot fully certify a stronger successor," **not** as any current method.
- **Schmidhuber's Gödel Machine (2003):** Jürgen Schmidhuber, *"Gödel Machines: Self-Referential Universal Problem Solvers Making Provably Optimal Self-Improvements,"* arXiv:cs/0309048. A formal self-improving agent that **rewrites any part of its own code once it has found a proof that the rewrite is beneficial** (increases expected future reward). Present as the clean formal endpoint of the self-modification lineage. URLs: `https://arxiv.org/abs/cs/0309048`; `https://people.idsia.ch/~juergen/goedelmachine.html`. **[SUBSTANCE confident; verify the "as soon as it has found a proof" phrasing against the abstract.]**

**Historical accuracy flag — "singularity" and von Neumann.** The term "singularity" for a runaway-progress point is often attributed to von Neumann via a **1958 obituary/tribute by Stanislaw Ulam**, who reported a conversation with von Neumann about "some essential singularity in the history of the race beyond which human affairs, as we know them, could not continue." **Von Neumann did not coin the modern technological-singularity usage**; the popular modern sense comes later (Vernor Vinge, 1993). Say so.

### 2c. Neuroplasticity: history and key figures (10 min)

- **Santiago Ramón y Cajal (c. 1894–1913):** the neuron doctrine; **early hints of plasticity** — he speculated that mental exercise could strengthen connections between neurons ("cerebral gymnastics"). The strong modern reading of Cajal as a plasticity pioneer is partly retrospective; present it as a *hint*, not a formal theory.
- **Donald O. Hebb (1949), *The Organization of Behavior* (Wiley), p. 62 — the Hebbian postulate. [VERBATIM — high confidence]:** *"When an axon of cell A is near enough to excite a cell B and repeatedly or persistently takes part in firing it, some growth process or metabolic change takes place in one or both cells such that A's efficiency, as one of the cells firing B, is increased."* Archive.org likely hosts a scan (test first).
- **Carla J. Shatz — "cells that fire together wire together."** **Attribution flag (get this right):** this famous mnemonic is **Shatz's paraphrase of Hebb**, not Hebb's own words. Source: Carla J. Shatz, *"The Developing Brain,"* *Scientific American* 267(3), September 1992, p. 64. Do **not** attribute the phrase to Hebb himself.
- **Eric Kandel:** *Aplysia* (sea slug) work establishing the **molecular/synaptic basis of learning and memory** — short-term memory via synaptic strength changes, long-term memory via gene expression and new synaptic growth (Nobel 2000).
- **Michael Merzenich:** experimental demonstration of **cortical map reorganization** in adult primates — sensory maps remodel with use/injury, overturning the "fixed adult brain" dogma.
- **Paul Bach-y-Rita:** **sensory substitution** (e.g., "seeing" through a tactile array on the skin/tongue) — dramatic evidence of cross-modal plasticity; his slogan "we see with our brains, not our eyes."
- **Norman Doidge (2007), *The Brain That Changes Itself*** — the popular synthesis that mainstreamed "neuroplasticity."
- **Metaplasticity — Wickliffe C. Abraham & Mark F. Bear (1996), "Metaplasticity: the plasticity of synaptic plasticity,"** *Trends in Neurosciences* 19(4), pp. 126–130. DOI `10.1016/S0166-2236(96)80018-X`. **The learning rule itself is modified by prior history** — plasticity of plasticity. *This is the neuroscience of a changing update rule* and is the single most important item in this block for the oversight argument.
- **Homeostatic/synaptic scaling — Gina Turrigiano et al. (1998), "Activity-dependent scaling of quantal amplitude in neocortical neurons,"** *Nature* 391, pp. 892–896 (DOI `10.1038/36103`); review: Turrigiano (2008), *Cell* 135(3), pp. 422–435 (DOI `10.1016/j.cell.2008.10.008`). Mechanism that **keeps Hebbian learning from running away** — a biological stabilizer/regularizer.
- **Stability–plasticity dilemma — Stephen Grossberg** (Adaptive Resonance Theory; e.g., "How does a brain build a cognitive code?", *Psychological Review* 87(1), 1980, pp. 1–51; Carpenter & Grossberg 1987): how does a system stay **plastic enough to learn new things** yet **stable enough not to overwrite old ones**? This is exactly **continual learning vs. catastrophic forgetting.**

**Interactive/visual resources for this block:** HHMI BioInteractive neuron/synapse animations (`https://www.hhmi.org/biointeractive`), LTP animations (search "LTP animation"), dendritic-spine growth microscopy videos on YouTube (search "dendritic spine growth two-photon"), and cortical-map reorganization figures from Merzenich reviews. **Test each; pre-load one LTP animation and one spine-growth clip.**

### 2d. The bridge — honest analysis (8 min; the intellectual heart of Block 2)

The organizer explicitly asked three questions. Answer them carefully.

**(i) Is there an analogy between Gödel numbering and neuroplasticity?**
- **Where it is strong:** Both are about systems in which *the representations are also the objects that act on the system.* In a Gödel-numbered system, a formula is both a statement and a number the system can compute over. In the brain, a synaptic weight is both *part of the computation* (it shapes activity) and *the thing that gets modified by* that same activity. In both, **the substrate and the description live in the same medium** — there is no clean outside "programmer."
- **Where it is weak (say this plainly):** Gödel numbering requires a **global, explicit, exact encoding** of the *entire system's syntax* such that the system can express precise self-referential propositions ("*this* sentence is not provable"). **Hebbian plasticity is local and has no global self-description** — a synapse "knows" only its own pre/post activity; there is no place in the brain that holds an exact encoded blueprint of the whole brain that the brain reads and rewrites. So the Gödel analogy is **at best partial.** The honest formulation: *both are systems whose representations are also the objects that act on the system — but only the formal system has an exact global self-encoding.*

**(ii) Do neuroplastic neurons have self-reference?**
- Candidate mechanisms for "self-reference": **recurrent connections** (the network's output feeds its own input), **efference copy / corollary discharge** (the motor system sends a copy of its command to predict sensory consequences), and the brain's **models of itself** (interoception, **body schema**, **metacognition**). These are real and important.
- **But is any of this self-reference in the Gödel sense?** Mostly **no**: they are **feedback and self-modeling**, not the encoding of an exact description of the system *inside* the system that the system can prove things about. Efference copy is a prediction signal, not a Gödel number of the motor cortex. Metacognition is an *approximate* model of one's own reliability, not a formal self-encoding. **The defensible line:** the brain has rich *self-modeling and feedback*; it does **not** have Gödel-style exact self-encoding. Feedback ≠ formal self-reference.

**(iii) How does neuroplasticity relate to self-improving AI?**
- **Gradient descent ↔ plasticity:** weight updates are the artificial analog of synaptic change.
- **Meta-learning / learned optimizers ("learning to learn") ↔ metaplasticity:** when the *update rule itself* is learned or changes with experience, that is the artificial mirror of Abraham & Bear's plasticity-of-plasticity.
- **Continual learning & catastrophic forgetting ↔ stability–plasticity dilemma (Grossberg) and homeostatic scaling (Turrigiano):** the same tension, and biology's stabilizers (scaling) are the conceptual cousins of regularization.
- **The oversight point (put on a slide):** *A system whose learning rule is fixed is far easier to predict and certify than one whose learning rule changes with experience.* Metaplasticity/learned-optimizers move the target: you are no longer overseeing a fixed learner but a learner-that-rewrites-how-it-learns. **Contrast the three architectures explicitly:**
  - **von Neumann's constructor:** copier B is **fixed**; description separate from machine; verbatim copy.
  - **DNA:** replication machinery **separate** from the genome; heritable mutations enable evolution.
  - **Neuroplasticity:** the modification rule is **itself modifiable** (metaplasticity) and there is **no separate, fixed copier** — the substrate rewrites itself in place.
  This progression — *fixed copier → separate machinery + mutation → self-modifying rule* — is a ladder of decreasing overseeability.

### 2e. Block 2 discussion points (for slides)
1. Gödel shows a system can **encode** itself but not fully **certify** itself. **What does that imply for a system asked to certify its own successor?** (Connect to Löb/soundness intuition — historical, not a method.)
2. Neuroplasticity shows the **learning rule itself can change.** **What would you need to observe to trust a system whose learning rule is changing?**
3. Is the brain's self-modeling (efference copy, body schema, metacognition) **self-reference, or just feedback?** Does the distinction matter for oversight?
4. Biology needs stabilizers (**synaptic scaling**) to keep Hebbian learning from exploding. **Is "stability that prevents runaway self-modification" a requirement for any overseeable self-improving system?**

---

# BLOCK 3 — Recursion & self-similarity (30 min)

**Suggested timing:** 5 min history + Mandelbrot quotes · 10 min live coding (Sierpiński recursion → chaos game → box-counting dimension) · 8 min scale invariance definition + measuring it in the Sierpiński triangle · 5 min scale invariance in vision · 2 min discussion.

### 3a. History (5 min)

- **Wacław Sierpiński (1915):** defined the triangle (and carpet) as classic self-similar sets.
- **Medieval precedent — Cosmatesque mosaics:** nested-triangle patterns matching the Sierpiński triangle appear in **13th-century Cosmati mosaic floors in Italy**, most famously the pavement of the **Cathedral of Anagni (Cattedrale di Anagni, Lazio, ~1226)** — predating Sierpiński by ~700 years. See the History section of `https://en.wikipedia.org/wiki/Sierpi%C5%84ski_triangle` and the scholarship on "Sierpinski triangles in stone" (Conversano & Tedeschini-Lalli). **[SUBSTANCE confident; verify the specific church/date on a primary art-history source.]**
- **Pascal's triangle mod 2:** color the odd entries of Pascal's triangle → the Sierpiński triangle emerges. A beautiful "same object, third route" demo (alongside recursion and the chaos game).
- **Benoit Mandelbrot, *The Fractal Geometry of Nature* (W.H. Freeman, 1982), p. 1 — [VERBATIM — high confidence]:** *"Clouds are not spheres, mountains are not cones, coastlines are not circles, and bark is not smooth, nor does lightning travel in a straight line."*
- **Mandelbrot (1967), "How Long Is the Coast of Britain? Statistical Self-Similarity and Fractional Dimension,"** *Science* 156(3775), 5 May 1967, pp. 636–638 (DOI `10.1126/science.156.3775.636`) — the **Richardson effect**: measured coastline length grows without bound as the ruler shrinks, which is what a fractional dimension formalizes.

### 3b. Live coding (10 min) — full runnable Python below (Section "CODE")

Walk through, in order: **(1)** recursive Sierpiński (base case + recursive step made explicit); **(2)** the **chaos game** (random iteration) producing *the same object from a non-recursive process* — a striking contrast; **(3)** **box-counting** dimension on a rasterized triangle, recovering **D = log 3 / log 2 ≈ 1.585.**

### 3c. Fractal dimension — the intuition (part of live coding)

**Similarity dimension:** if a shape is made of **N** copies of itself each scaled down by factor **s**, then **D = log N / log s.** For the Sierpiński triangle, **N = 3** copies at scale factor **1/s = 1/2**, so **D = log 3 / log 2 ≈ 1.585.** It is "more than a line, less than a plane."

**Box counting (the empirical version):** overlay grids of box size ε; count the number **Nの(ε)** of boxes that contain any part of the shape. For a fractal, **N(ε) ∝ ε^(−D)**, so a **log N(ε) vs. log(1/ε)** plot is a straight line whose **slope is D.** This is the practical method used on real (non-idealized) images.

### 3d. Scale invariance (8 min)

**Definition:** a structure or statistic is **scale-invariant** if it looks the same (exactly, or statistically) under rescaling. The mathematical signature is a **power law:** f(kx) = k^a f(x). Power laws are the only functions with no characteristic scale.

**Measuring it in the Sierpiński triangle:**
- **Box-count vs. box-size on log-log axes** → a straight line of slope −D (this *is* the scale-invariance measurement).
- **Mass–radius relation:** mass enclosed within radius r scales as r^D.
- **A crucial subtlety to state (exact vs. statistical self-similarity):** the Sierpiński triangle's self-similarity is **exact and discrete** — it reproduces itself *only* at scale factors of **2ⁿ**, not at every continuous magnification. This differs from **statistical, continuous scale invariance** in nature (coastlines, clouds, natural images), which is approximate and holds across a *continuous* range of scales. Great discussion contrast.

### 3e. Scale invariance in vision (5 min)

**Natural image statistics.**
- **David J. Field (1987), "Relations between the statistics of natural images and the response properties of cortical cells,"** *JOSA A* 4(12), pp. 2379–2394 (DOI `10.1364/JOSAA.4.002379`): natural images have approximately **1/f² power spectra** (amplitude ∝ 1/f), i.e., **scale-invariant second-order statistics.** Field argued cortical simple cells (oriented, multi-scale, band-pass — Gabor-like) are **matched to** this structure, giving a *sparse, efficient code.*
- **Daniel Ruderman & William Bialek (1994), "Statistics of natural images: Scaling in the woods,"** *Physical Review Letters* 73(6), pp. 814–817 (DOI `10.1103/PhysRevLett.73.814`): natural-scene statistics exhibit **scaling/self-similarity** across spatial scales — the "scaling in the woods" result. (See also Ruderman 1997.)
- **Why it matters:** if the world's images are scale-invariant, an efficient visual system should be **built to exploit that** — motivating multi-scale representations.

**Multi-scale machinery (biological and artificial).**
- **Campbell & Robson (1968), "Application of Fourier analysis to the visibility of gratings,"** *J. Physiol.* 197(3), pp. 551–566 (DOI `10.1113/jphysiol.1968.sp008574`): psychophysical evidence for **independent spatial-frequency channels** in V1 — the visual system decomposes images into multiple scale bands.
- **Scale-space theory:** Witkin (1983), Koenderink (1984, "The structure of images," *Biol. Cybern.*), Lindeberg (1994) — representing an image at all scales via Gaussian smoothing.
- **Image pyramids:** Burt & Adelson (1983), "The Laplacian Pyramid as a Compact Image Code," *IEEE Trans. Communications* — Gaussian/Laplacian pyramids.
- **SIFT — David G. Lowe (2004), "Distinctive Image Features from Scale-Invariant Keypoints,"** *IJCV* 60(2), pp. 91–110 (DOI `10.1023/B:VISI.0000029664.99615.94`; author copy `https://www.cs.ubc.ca/~lowe/papers/ijcv04.pdf` — **test**): explicitly **scale-invariant** keypoints via difference-of-Gaussian scale space.
- **CNNs & feature pyramids:** convolutional nets and FPN-style architectures handle scale via pooling/strides and multi-resolution feature maps (mention as the modern echo — *not* as an alignment method).
- **Biological scale handling:** **receptive-field sizes increase with eccentricity** and up the visual hierarchy; **size constancy**; and the **retinotopic log-polar mapping — Eric Schwartz (1977), "Spatial mapping in the primate sensory projection,"** *Biological Cybernetics* 25(4), pp. 181–194 (DOI `10.1007/BF01885636`): the cortical map is approximately **log-polar**, which converts **scaling and rotation about the fovea into translation** — a beautiful architectural trick that makes scale/rotation invariance nearly "free."

### 3f. Block 3 discussion points (for slides)
1. Recursion = **base case + inductive step.** **What is the analog for a system that improves itself** — what is the "base case," and what is the "step," and does the recursion terminate?
2. **Exact vs. statistical self-similarity:** capability growth (and oversight difficulty) is presumably *statistical*, not exact. Does that make it easier or harder to reason about?
3. **Does oversight need to be scale-invariant?** Does supervising a more capable system *look the same* at every capability scale (self-similar difficulty), or are there **phase transitions** where the whole nature of the problem changes?
4. Vision solves scale by building **explicit multi-scale representations.** Is the analog for oversight to build overseers at every capability scale?

---

# CLOSING — defocused cross-cutting discussion (put all on slides; pick 4–6)

1. **The copy/interpret lever.** Von Neumann separated *copying* a description (verbatim, uninterpreted) from *interpreting* it (constructing). **Is that separation a lever for oversight** — could you inspect or gate the "interpretation" step while letting the "copy" step run, or vice versa?
2. **The unrecallable system.** Dyson's Astrochicken and Sagan–Newman's runaway probe **cannot be recalled once launched.** What is the AI analog of "launch," and is there an analog of a recall mechanism — or is irreversibility intrinsic?
3. **Encode vs. certify.** Gödel shows a system can **encode** itself but not fully **certify** its own consistency. **What does that imply for any system asked to certify the safety of a successor more capable than itself?**
4. **Reproduction vs. improvement.** Verbatim self-copying is not improvement; **improvement needs heritable variation + selection.** Which is actually the thing we fear in "self-improving AI" — the copying, or the selection pressure?
5. **A changing learning rule.** Metaplasticity shows the update rule itself can change. **What evidence would let you trust a system whose learning rule is changing** in ways you did not specify?
6. **Stabilizers as a safety requirement.** Biology *needs* homeostatic scaling to stop Hebbian learning from exploding. **Is a built-in stabilizer against runaway self-modification a necessary property of any overseeable self-improving system?**
7. **Self-reference vs. feedback.** The brain models itself (efference copy, body schema, metacognition) without Gödel-style exact self-encoding. **Which kind of "self-knowledge" matters for oversight — exact self-description, or good-enough self-modeling?**
8. **Scale invariance of difficulty.** Is oversight **self-similar** (same difficulty shape at every capability scale) or does it have **phase transitions**? If there are phase transitions, where might they be?
9. **The threshold.** Von Neumann's complexity threshold separates *degenerative* from *self-sustaining* construction. **Is there an analogous threshold for self-improvement, and would we recognize it before or after crossing it?**
10. **The description in two readings.** In DNA, quines, and von Neumann's tape, the same description is *run* and *copied*. **Does an AI have a "description of itself" that is read in two ways, and does supervising each reading require different tools?**
11. **Who completes the description?** Von Neumann's own theory reached us only because **Burks reconstructed it.** If understanding a system requires a second party to "complete its description," what does that say about self-certification?
12. **The docility caveat.** Good's 1965 line ends "*provided that the machine is docile enough to tell us how to keep it under control.*" **Is that proviso doing all the work — and is it a property we could ever verify from the outside?**

---

# CURATED INTERACTIVE VISUALS & VIDEOS (grouped by block)
> **Test every link before the session; do not project an unopened URL.**

**Block 1 — self-reproduction**
- **Golly CA simulator** — `https://golly.sourceforge.net/` (desktop) and web app `https://golly.sourceforge.net/webapp/golly.html`. *On screen:* load von Neumann's 29-state rule + a Nobili–Pesavento self-rep pattern; step it to show the constructor arm building and the tape being copied.
- **Conway's Game of Life in-browser** — `https://playgameoflife.com/`. *On screen:* warm-up on emergence before showing the far more complex von Neumann rule.
- **Elementary CA reference (Wolfram MathWorld)** — `https://mathworld.wolfram.com/ElementaryCellularAutomaton.html`. *On screen:* Rule 90 → the Sierpiński triangle (a bridge to Block 3).
- **YouTube:** search `von Neumann universal constructor Golly` / `Nobili Pesavento self-replicating`. *On screen:* a 60–90 s clip of the constructor replicating. (Pick and pre-load one; specific ID unverified.)

**Block 2 — self-reference & plasticity**
- **HHMI BioInteractive** — `https://www.hhmi.org/biointeractive` (neuron/synapse/LTP animations). *On screen:* an LTP animation while stating Hebb's postulate.
- **Dendritic-spine growth microscopy** — YouTube search `dendritic spine growth two-photon`. *On screen:* live structural plasticity as the physical face of "wiring changes."
- **Quine explorer / online interpreter** — write and run a one-line quine live (e.g., in Python: see code note below) to demonstrate instructions-vs-data on screen.
- **Nicky Case explorables** — `https://ncase.me/` (interactive systems/feedback explorables) for a feedback-vs-self-reference discussion prop.

**Block 3 — recursion, fractals, scale**
- **Fractal generator (in-browser)** — `https://sciencevsmagic.net/fractal/`. *On screen:* draw a Sierpiński-type fractal live and change depth.
- **GeoGebra chaos game / Sierpiński** — `https://www.geogebra.org/` (search "chaos game Sierpinski"). *On screen:* run the random-iteration chaos game and watch the triangle emerge from randomness.
- **Coastline paradox** — `https://en.wikipedia.org/wiki/Coastline_paradox` and Observable notebooks (`https://observablehq.com/`, search "coastline"). *On screen:* shrink the ruler, watch measured length grow (Richardson effect).
- **Mandelbrot deep-zoom video** — YouTube search `Mandelbrot deep zoom`. *On screen:* 60 s of infinite self-similar zoom to make scale invariance visceral.
- **Complexity Explorables** — `https://www.complexity-explorables.org/` (fractal/CA explorables). *On screen:* a box-counting or fractal explorable if one is live.
- **Image pyramids** — OpenCV tutorial `https://docs.opencv.org/` ("Image Pyramids"). *On screen:* a Gaussian/Laplacian pyramid to motivate multi-scale vision.

---

# SLIDE-BY-SLIDE OUTLINE (≈32 slides)

**Opening (3 slides)**
1. **Title** — "Self-Improving Systems: A Historical Lead-in to Scalable Oversight." Bullets: UIUC hook (von Neumann lectured here, Dec 1949); three lenses; ground rule (no current methods). Prompt: "What makes a capable system hard to supervise?"
2. **The problem** — Scalable oversight defined; Amodei et al. 2016 (arXiv:1606.06565). Bullets: judge outputs we can't cheaply evaluate; overseer weaker than system; interaction with self-reproduction/modification. Quote: Amodei et al. scalable-oversight definition **[verify]**.
3. **The four properties & three blocks** — self-reference (Gödel), self-modification (plasticity), self-reproduction (von Neumann), scale (fractals). Prompt: which property worries you most?

**Block 1 (8 slides)**
4. **Who was von Neumann** — Budapest 1903 → IAS → Manhattan Project → EDVAC → Illinois 1949 → d. 1957. Visual: portrait. Prompt: why did *this* polymath turn to self-reproduction?
5. **Who was Dyson** — Cambridge/Cornell/IAS; QED; Orion; Dyson sphere; d. 2020; IAS contemporary of von Neumann. Visual: portrait.
6. **From Hixon 1948 to Illinois 1949 to Burks 1966** — the lecture lineage; Burks reconstructed the text. Bullet: the canonical text is itself a completed description. Prompt: what's lost when a second author completes your theory?
7. **The universal constructor** — A (build), B (copy verbatim), C (control), φ(A+B+C) (tape). Visual: block diagram. Prompt: why doesn't the blueprint need a blueprint of itself?
8. **Two models** — kinematic vs. 29-state CA. Visual/link: **Golly** running the Nobili–Pesavento pattern. Prompt: what does the CA model buy us over the kinematic one?
9. **Description read twice = DNA** — instructions (transcription) vs. data (replication); anticipated Watson–Crick 1953. Quote: Brenner on von Neumann anticipating the code **[PARAPHRASE — reconstruct]**. Prompt: is "copy" separable from "interpret" for oversight?
10. **The complexity threshold** — below: degenerative; above: self-sustaining/explosive; mutations in the tape are inherited → evolution. Quote: threshold passage **[PARAPHRASE — pull from Hixon/Burks]**. Prompt: reproduction vs. improvement — what's the difference?
11. **Astrochicken & runaway probes** — Dyson's ~1 kg egg-grown probe; Tipler 1980 vs. Sagan & Newman 1983 (runaway danger); berserkers. Quote: Sagan–Newman danger **[verify]**. Link: Mandelbrot/CA video optional. Prompt: what is oversight once it has left?

**Block 2 (10 slides)**
12. **Gödel 1931** — numbering; diagonal lemma; "I am not provable"; encode-but-not-certify. Quote: Gödel opening **[verify translation]**; SEP link. Prompt: what can't a system prove about itself?
13. **Kleene, quines, and von Neumann's tape** — recursion theorem; a program can read its own code; φ is a Gödel-like encoding. *Live:* run a quine. Prompt: are self-rep, quines, and the Gödel sentence "the same trick"?
14. **Hofstadter's strange loops** — top level reaches down to bottom level. Quote: GEB strange-loop passage **[VERBATIM, verify page]**.
15. **The self-modifying-machine lineage I** — Turing 1950 child machine; Turing 1951 "take control." Quote: Turing 1951 **[VERBATIM, verify vs. AMT/B/4]**. Flag: paraphrases circulate.
16. **The self-modifying-machine lineage II** — Good 1965 intelligence explosion. Quote: Good full passage **[VERBATIM]**. Prompt: note the "docile enough to keep under control" caveat.
17. **Formal self-modification** — Löb (historical, soundness intuition); Schmidhuber's Gödel Machine (rewrites code on a proof of improvement). Quote: Gödel Machine **[verify]**. Flag: "singularity" not coined by von Neumann (Ulam 1958 report; Vinge 1993 modern sense).
18. **Neuroplasticity: the postulate** — Cajal hints; Hebb 1949. Quote: Hebb postulate **[VERBATIM]**. Attribution flag: "fire together wire together" = **Shatz 1992**, not Hebb.
19. **Neuroplasticity: mechanisms & people** — Kandel (Aplysia), Merzenich (cortical maps), Bach-y-Rita (sensory substitution), Doidge. Link: LTP animation; spine-growth video.
20. **The rule that changes the rule** — metaplasticity (Abraham & Bear 1996); homeostatic scaling (Turrigiano 1998/2008); stability–plasticity dilemma (Grossberg). Prompt: what stops learning from running away?
21. **Bridge: Gödel vs. plasticity — honest scorecard** — strong: representations are also the actors; weak: no global exact self-encoding in the brain. Self-reference vs. feedback (efference copy, body schema, metacognition). Prompt: which self-knowledge matters for oversight?
22. **Bridge: plasticity → self-improving AI** — gradient descent≈plasticity; meta-learning≈metaplasticity; continual learning≈stability-plasticity; **fixed rule easier to oversee than a self-changing rule.** Table: von Neumann (fixed copier) vs. DNA (separate machinery + mutation) vs. brain (self-modifying rule). Prompt: trust criteria for a changing learning rule?

**Block 3 (8 slides)**
23. **Sierpiński: three routes, one object** — 1915 definition; Anagni/Cosmati 13th-c. mosaics; Pascal mod 2. Visual: the three constructions side by side. Prompt: why does the same shape appear from recursion, randomness, and arithmetic?
24. **Mandelbrot & roughness** — "Clouds are not spheres…"; coastline 1967 (Richardson effect). Quote: Mandelbrot opening **[VERBATIM]**. Link: coastline paradox interactive.
25. **Live code 1: recursive Sierpiński** — base case + recursive step. *Live:* run it. Prompt: where's the base case for a self-improving system?
26. **Live code 2: the chaos game** — same object from a non-recursive random process. *Live:* run it. Prompt: recursion vs. emergence — does the mechanism matter?
27. **Fractal dimension** — D = log N/log s = log 3/log 2 ≈ 1.585; box counting; N(ε) ∝ ε^(−D). *Live:* run box-count, show log-log line. Prompt: what does "1.585 dimensions" mean?
28. **Scale invariance** — power laws f(kx)=k^a f(x); exact/discrete (2ⁿ only) vs. statistical/continuous in nature. Prompt: is capability growth exact or statistical self-similarity?
29. **Scale in natural images** — 1/f² spectra (Field 1987); scaling in the woods (Ruderman & Bialek 1994); vision matched to image statistics. Prompt: should overseers be "matched" to the systems they watch?
30. **Multi-scale vision** — Campbell & Robson 1968 (frequency channels); scale-space/pyramids (Burt & Adelson 1983); SIFT (Lowe 2004); log-polar map (Schwartz 1977) turns scaling into translation. Link: image-pyramid demo. Prompt: is the fix for scale "build an overseer at every scale"?

**Closing (2 slides)**
31. **Cross-cutting questions I** — copy/interpret lever; unrecallable launch; encode≠certify; reproduction vs. improvement; changing learning rule; stabilizers.
32. **Cross-cutting questions II + wrap** — self-reference vs. feedback; scale-invariance of difficulty & phase transitions; the threshold; Good's "docility" proviso. Closing line: oversight is the problem of controlling systems that reference, modify, reproduce, and scale themselves.

---

# CODE (ready to run)

```python
# ============================================================
# Block 3 live demos: Sierpinski via recursion, chaos game,
# and a box-counting fractal-dimension estimate.
# Requires: numpy, matplotlib.  Tested logic; run top to bottom.
# ============================================================

import numpy as np
import matplotlib.pyplot as plt


# ------------------------------------------------------------
# (1) RECURSIVE SIERPINSKI TRIANGLE
#     Base case + inductive step made explicit.
# ------------------------------------------------------------
def sierpinski_recursive(ax, p1, p2, p3, depth):
    """Draw a Sierpinski triangle by recursion.
    Base case: depth == 0  -> fill the triangle (p1,p2,p3).
    Recursive step: split into 3 corner sub-triangles using
    edge midpoints, recurse on each with depth-1.
    """
    if depth == 0:                                   # BASE CASE
        tri = plt.Polygon([p1, p2, p3], edgecolor='none')
        ax.add_patch(tri)
        return
    m12 = (p1 + p2) / 2.0                             # midpoints
    m23 = (p2 + p3) / 2.0
    m31 = (p3 + p1) / 2.0
    sierpinski_recursive(ax, p1,  m12, m31, depth - 1)  # INDUCTIVE STEP
    sierpinski_recursive(ax, m12, p2,  m23, depth - 1)
    sierpinski_recursive(ax, m31, m23, p3,  depth - 1)


def draw_recursive(depth=6):
    p1 = np.array([0.0, 0.0])
    p2 = np.array([1.0, 0.0])
    p3 = np.array([0.5, np.sqrt(3) / 2.0])
    fig, ax = plt.subplots(figsize=(6, 6))
    sierpinski_recursive(ax, p1, p2, p3, depth)
    ax.set_aspect('equal'); ax.axis('off')
    ax.set_title(f'Recursive Sierpinski (depth={depth}): '
                 f'{3**depth} triangles')
    plt.show()


# ------------------------------------------------------------
# (2) CHAOS GAME (random iteration)
#     Same object from a NON-recursive stochastic process.
# ------------------------------------------------------------
def chaos_game(n_points=100_000, seed=0):
    rng = np.random.default_rng(seed)
    verts = np.array([[0.0, 0.0],
                      [1.0, 0.0],
                      [0.5, np.sqrt(3) / 2.0]])
    pt = np.array([0.5, 0.25])          # any starting point
    xs = np.empty(n_points); ys = np.empty(n_points)
    for i in range(n_points):
        v = verts[rng.integers(0, 3)]   # pick a random vertex
        pt = (pt + v) / 2.0             # jump halfway toward it
        xs[i], ys[i] = pt
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.scatter(xs, ys, s=0.1, marker='.', linewidths=0)
    ax.set_aspect('equal'); ax.axis('off')
    ax.set_title(f'Chaos game: {n_points:,} points')
    plt.show()
    return xs, ys


# ------------------------------------------------------------
# (3) BOX-COUNTING FRACTAL DIMENSION
#     Rasterize a Sierpinski triangle (via chaos game),
#     count occupied boxes at scales eps = 1/2^k,
#     slope of log N(eps) vs log(1/eps) estimates D.
#     Expected: D -> log(3)/log(2) ~= 1.585
# ------------------------------------------------------------
def rasterize_chaos(n_points=2_000_000, grid=1024, seed=1):
    rng = np.random.default_rng(seed)
    verts = np.array([[0.0, 0.0],
                      [1.0, 0.0],
                      [0.5, np.sqrt(3) / 2.0]])
    pt = np.array([0.5, 0.25])
    img = np.zeros((grid, grid), dtype=bool)
    xmin, xmax = 0.0, 1.0
    ymin, ymax = 0.0, np.sqrt(3) / 2.0
    for _ in range(n_points):
        v = verts[rng.integers(0, 3)]
        pt = (pt + v) / 2.0
        ix = int((pt[0] - xmin) / (xmax - xmin) * (grid - 1))
        iy = int((pt[1] - ymin) / (ymax - ymin) * (grid - 1))
        img[iy, ix] = True
    return img


def box_count_dimension(img):
    """Estimate box-counting dimension of a boolean image whose
    side length is a power of two."""
    n = img.shape[0]
    assert (n & (n - 1)) == 0, "use a power-of-two grid size"
    sizes, counts = [], []
    box = 1
    while box <= n:
        # reshape into (n/box, box, n/box, box) and test any-occupied
        reshaped = img.reshape(n // box, box, n // box, box)
        occupied = reshaped.any(axis=(1, 3))
        counts.append(int(occupied.sum()))
        sizes.append(box)
        box *= 2
    sizes = np.array(sizes)
    counts = np.array(counts)
    # log N(eps) vs log(1/eps); slope = D. eps = box/n.
    x = np.log(1.0 / (sizes / img.shape[0]))
    y = np.log(counts)
    # Fit on the linear (scaling) middle range; drop the smallest
    # boxes (pixelation floor) and the largest boxes (finite size).
    lo, hi = 2, len(sizes) - 1
    slope, intercept = np.polyfit(x[lo:hi], y[lo:hi], 1)
    return slope, (x, y)


def demo_dimension():
    img = rasterize_chaos()
    D, (x, y) = box_count_dimension(img)
    print(f"Estimated box-counting dimension D = {D:.4f}")
    print(f"Theoretical D = log(3)/log(2) = {np.log(3)/np.log(2):.4f}")
    fig, ax = plt.subplots(figsize=(6, 5))
    ax.plot(x, y, 'o-', label='box counts')
    ax.set_xlabel('log(1/eps)'); ax.set_ylabel('log N(eps)')
    ax.set_title(f'Box counting: slope ~= D = {D:.3f}')
    ax.legend(); plt.show()


if __name__ == "__main__":
    draw_recursive(depth=6)     # (1)
    chaos_game()                # (2)
    demo_dimension()            # (3)
```

**Optional live quine for Block 2** (demonstrates instructions-vs-data on screen):
```python
s = 's = %r\nprint(s %% s)'
print(s % s)
```
Running it prints its own source — the program used *as instructions* (run) and *as data* (reproduced), von Neumann's φ in miniature.

---

# GO-DEEPER READING LIST (primary sources first)
> Test each URL; several are behind paywalls (DOIs given so students can use library access).

**Primary**
- **John von Neumann,** *Theory of Self-Reproducing Automata*, ed. Arthur W. Burks (University of Illinois Press, 1966). Search archive.org: `Theory of Self-Reproducing Automata von Neumann`.
- **John von Neumann,** "The General and Logical Theory of Automata," in *Cerebral Mechanisms in Behavior: The Hixon Symposium*, ed. L.A. Jeffress (Wiley, 1951), pp. 1–41.
- **Freeman Dyson,** *Infinite in All Directions* (Harper & Row, 1988) — Astrochicken; and *Disturbing the Universe* (Harper & Row, 1979) — von Neumann anecdotes, early self-reproducing machines.
- **Kurt Gödel,** "On Formally Undecidable Propositions…" (1931), trans. in van Heijenoort (ed.), *From Frege to Gödel* (Harvard, 1967), pp. 596–616.
- **Donald O. Hebb,** *The Organization of Behavior* (Wiley, 1949) — postulate on p. 62.
- **Benoit Mandelbrot,** *The Fractal Geometry of Nature* (W.H. Freeman, 1982); and "How Long Is the Coast of Britain?", *Science* 156(3775), 1967, pp. 636–638 (DOI `10.1126/science.156.3775.636`).
- **David J. Field,** "Relations between the statistics of natural images and the response properties of cortical cells," *JOSA A* 4(12), 1987 (DOI `10.1364/JOSAA.4.002379`).
- **David G. Lowe,** "Distinctive Image Features from Scale-Invariant Keypoints," *IJCV* 60(2), 2004 (DOI `10.1023/B:VISI.0000029664.99615.94`; `https://www.cs.ubc.ca/~lowe/papers/ijcv04.pdf`).

**Secondary / historical**
- **Douglas Hofstadter,** *Gödel, Escher, Bach* (Basic Books, 1979).
- **I.J. Good,** "Speculations Concerning the First Ultraintelligent Machine," *Advances in Computers* 6, 1965, pp. 31–88.
- **A.M. Turing,** "Computing Machinery and Intelligence," *Mind* 59, 1950 (DOI `10.1093/mind/LIX.236.433`); and "Intelligent Machinery, A Heretical Theory" (c.1951), in Copeland (ed.), *The Essential Turing* (OUP, 2004); Turing Digital Archive `https://turingarchive.kings.cam.ac.uk/`.
- **Jürgen Schmidhuber,** "Gödel Machines…" arXiv:cs/0309048 (`https://people.idsia.ch/~juergen/goedelmachine.html`).
- **W.C. Abraham & M.F. Bear,** "Metaplasticity," *TINS* 19(4), 1996 (DOI `10.1016/S0166-2236(96)80018-X`).
- **G.G. Turrigiano** et al., *Nature* 391, 1998 (DOI `10.1038/36103`); review, *Cell* 135(3), 2008 (DOI `10.1016/j.cell.2008.10.008`).
- **U. Pesavento,** "An Implementation of von Neumann's Self-Reproducing Machine," *Artificial Life* 2(4), 1995, pp. 337–354.
- **F. Tipler,** *QJRAS* 21, 1980, pp. 267–281; **C. Sagan & W. Newman,** *QJRAS* 24, 1983, pp. 113–121.
- **D. Ruderman & W. Bialek,** "Statistics of natural images: Scaling in the woods," *PRL* 73(6), 1994 (DOI `10.1103/PhysRevLett.73.814`).
- **F.W. Campbell & J.G. Robson,** *J. Physiol.* 197(3), 1968 (DOI `10.1113/jphysiol.1968.sp008574`); **E. Schwartz,** *Biol. Cybern.* 25(4), 1977 (DOI `10.1007/BF01885636`); **Burt & Adelson,** "The Laplacian Pyramid as a Compact Image Code," *IEEE Trans. Comm.*, 1983.
- **Amodei et al.,** "Concrete Problems in AI Safety," arXiv:1606.06565.
- **Norman Doidge,** *The Brain That Changes Itself* (Viking, 2007) — popular neuroplasticity.

---

## DISPUTED / OFTEN-MISATTRIBUTED CLAIMS — GET THESE RIGHT (put a "myth-busting" note on a slide)
- **"Cells that fire together wire together"** is **Carla Shatz's** 1992 mnemonic paraphrase, **not** Hebb's own words. Hebb's actual 1949 sentence is the "axon of cell A…" passage.
- **Von Neumann did not coin the modern "technological singularity."** The often-cited phrasing comes from **Stanislaw Ulam's 1958 tribute** reporting a conversation ("essential singularity in the history of the race"); the modern usage is **Vernor Vinge (1993)**.
- **Turing's 1951 "take control" line** exists, but multiple **paraphrases circulate**; verify the exact wording against the manuscript (Turing Digital Archive, AMT/B/4) before quoting verbatim.
- **Sierpiński "invented" the triangle in 1915**, but the pattern appears in **13th-century Cosmati mosaics** (e.g., Anagni Cathedral) centuries earlier — Sierpiński formalized it, he did not first draw it.
- **Von Neumann "anticipated DNA":** true in the *logical* sense (description used as instructions and data, before Watson–Crick 1953), but he did not describe the chemistry; keep the claim about *logic*, not *molecular structure*.

---

## CAVEATS
1. **Tooling limitation.** The automated search/fetch tools were non-operational during preparation, so **no quotation here was checked against a live page and no URL was liveness-tested.** Every quote is tagged by confidence; **[VERBATIM]** items (Hebb, Good, Mandelbrot opening, Hofstadter strange loop, Turing "take control") are high-confidence but still merit a page check; **[PARAPHRASE]** items (von Neumann's threshold sentence, Brenner on the genetic code, the Astrochicken descriptive wording, Sagan–Newman) **must be reconstructed from the primary text before being shown as quotations.** The presenter should spend ~30–45 minutes verifying quotes and links against the primary sources listed.
2. **Amodei et al. definition.** The exact one-sentence scalable-oversight definition should be pulled verbatim from the arXiv PDF; the version here is substance-accurate but not guaranteed word-for-word.
3. **Golly contents.** Golly historically ships von Neumann's 29-state rule and Nobili–Pesavento patterns; confirm they are present in the version you install before promising a live demo, and have a pre-recorded video as backup.
4. **Bibcodes/DOIs.** ADS bibcodes for Tipler (1980) and Sagan & Newman (1983) and some DOIs are given from memory; verify before printing on a reading list.
5. **Scope discipline.** By design this primer contains **no current alignment methods.** If the discussion drifts to specific modern techniques, redirect to the conceptual question underneath it — that is the point of a history-and-concepts session.
6. **Analogy honesty.** The Gödel–neuroplasticity analogy is deliberately presented as **partial**: both are systems whose representations are also the actors, but only formal systems have exact global self-encoding, and Hebbian plasticity is local with no global self-description. Do not oversell it.
