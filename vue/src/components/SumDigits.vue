<template>
<div class="sum-digits">
  <h1> Sum the digits in paragraphs. </h1>
  <Input v-model.lazy="queryString" type="textarea" :autosize="{minRows:10}" @on-change="handleNewRequest" />
  answer is: {{ computedAnswer }}
</div>
</template>

<script lang="ts">
import Vue, {
  PropType
} from 'vue';

export default Vue.extend({
  data() {
    return {
      queryString: '' as string,
      answer: null as number | null,
    };
  },
  computed: {
    computedAnswer(): number | string {
      if(this.answer === null) {
        return '';
      }
      return this.answer;
    }
  },
  methods: {
    handleNewRequest() {
      const vm: any = this;
      vm.axios.post('api/parse/sumDigit', {
        content: vm.queryString
      }).then((response: any) => {
        vm.answer = response.data
      })
    }
  }

})
</script>

<style scoped lang="less">
</style>
