<template>
<div class="rsna-standard-template-container">
  <header class="bg-inverse">
    <h1>
      RSNA Standard Template
    </h1>

    <label class="custom-control custom-checkbox">
      <input v-model="showFancyTemplate" type="checkbox" class="custom-control-input">
      <span class="custom-control-indicator"></span>
      <span class="custom-control-description">Eye Candy</span>
    </label>

    <button class="btn btn-lg btn-warning"
      @click='exportRSNA()'
      >
      Export
    </button>
  </header>

  <rsna-standard-fancy v-if="showFancyTemplate" :rsna="rsna"></rsna-standard-fancy>
  <div v-else>
    <section id="technical-parameters">
      <h2>Technical parameters</h2>
      <article>
        <!-- {{technical}} -->
        <olp label='kVp' :value='technical.kVp.value'></olp>
        <olp label='mA' :value='technical.mA.value'></olp>
        <olp label='DLP' :value='technical.DLP.value + " " + technical.DLP.unit'></olp>
      </article>
    </section>

    <section id="clinical-information">
      <h2>Clinical information</h2>
      <article>
        <!-- {{clinical}} -->
        <olp label='Screening visit' :value='clinical.visit'></olp>
        <p>
          {{ clinical.reason }}
        </p>
      </article>
    </section>

    <section id="findings">
      <h2>Findings</h2>
      <!-- {{findings}} -->

      <article>
        <!-- {{ findings.exam }} -->
        <h3>Exam parameters</h3>
        <olp label='Diagnostic quality' :value='findings.exam.diagnosticQuality'></olp>
        <olp label='Comments' :value='findings.exam.comments'></olp>
      </article>

      <article>
        <!-- {{findings.lungNodules}} -->
        <h3>Lung nodules</h3>
        <p v-if="findings.lungNodules.length === 0">
          None.
        </p>

        <div class="nodule-list" v-else>
          <nodule v-for="(nodule, index) in findings.lungNodules" :nodule="nodule" :index="index">
            <div slot="add-on-editor">
              {{ nodule }}
            </div>
          </nodule>
        </div>

      </article>

      <article>
        {{findings.lungs}}
        <h3>Lungs</h3>

      </article>

      <article>
        {{findings.rightPleuralSpace}}
        <h3>Right pleural space</h3>
      </article>

      <article>
        {{findings.leftPleuralSpace}}
        <h3>Left pleural space</h3>
      </article>

      <article>
        {{findings.heart}}
        <h3>Heart</h3>
      </article>

      <article>
        {{findings.other}}
        <h3>Other findings</h3>
      </article>

    </section>

    <section id="impression">
      <h2>Impression</h2>
      <!-- {{ impression }} -->
      <article>
        <olp label='Need comparison' :value='impression.needComparison'></olp>
        <olp label='Repeat CT' :value='impression.repeatCT'></olp>
        <olp label='See physician' :value='impression.seePhysician'></olp>
        <olp label='See physician' :value='impression.comments'></olp>
      </article>
    </section>
  </div>

</div>
</template>

<script>
import RSNAStandardTemplateFancy from './RSNAStandardTemplateFancy'

import OneLineParagraph from './OneLineParagraph'

import Nodule from '../annotate-and-segment/Nodule'

export default {
  components: {
    'rsna-standard-fancy': RSNAStandardTemplateFancy,
    'olp': OneLineParagraph,
    Nodule
  },
  data () {
    return {
      showFancyTemplate: false,
      ...this.rsna
    }
  },
  props: [ 'rsna' ],
  methods: {
    exportRSNA () {

    }
  }
}
</script>

<style lang="scss" scoped>
.rsna-standard-template-container {

  header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    color: white;
    padding-left: 2em;
    font-weight: normal;
    letter-spacing: 2px;
		margin-bottom: 10px;

    padding-right: 10%;

    h1 {
      font-size: 2.5em;

      line-height: 2em;
      margin: 0;
    }
  }

  .custom-control {
    margin: 0;
  }

  h2 {
    padding-top: 0.5em;
    margin-bottom: 1em;
  }

  section {
    padding-left: 2em;
    margin-bottom: 3em;
  }

  article {
    margin-left: 1em;
    font-size: 1.35em;
    h3 {
      margin-bottom: 1em;
    }
    p {
      margin-left: 1em;
    }

    .nodule-list {
      padding: 0 1em;
    }
  }

  .flex-space-around {
    display: flex;
    justify-content: space-around;
  }
}
</style>
