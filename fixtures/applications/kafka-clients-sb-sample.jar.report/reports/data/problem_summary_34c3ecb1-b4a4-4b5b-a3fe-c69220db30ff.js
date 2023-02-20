MIGRATION_ISSUES_DETAILS["34c3ecb1-b4a4-4b5b-a3fe-c69220db30ff"] = [
{description: "<p>Replace the Spring Web artifact with Quarkus <code>spring-web<\/code> extension<\/p><p>Spring Web is a spring-web artifact brought transitively by any <code>org.springframework:spring-web*<\/code> dependency<br/>Add Quarkus dependency <code>io.quarkus:quarkus-spring-web<\/code> <\/p><p>Starting with Quarkus version 2.5, the underlying JAX-RS engine must be chosen. For performance reasons, the <code>quarkus-resteasy-reactive-jackson<\/code> dependency should be used.<\/p>", ruleID: "springboot-web-to-quarkus-00000", issueName: "Replace the Spring Web artifact with Quarkus \'spring-web\' extension",
problemSummaryID: "34c3ecb1-b4a4-4b5b-a3fe-c69220db30ff", files: [
{l:"<a class='' href='pom_xml.html?project=4423800'>META-INF/maven/com.rmarting.kafka/kafka-clients-sb-sample/pom.xml<\/a>", oc:"1"},
], resourceLinks: [
{h:"https://github.com/quarkusio/quarkus/wiki/Migration-Guide-2.5#spring-web", t:"Quarkus Migration Guide 2.5"},
{h:"https://quarkus.io/guides/spring-web", t:"Quarkus Spring Web Guide"},
]},
];
onProblemSummaryLoaded("34c3ecb1-b4a4-4b5b-a3fe-c69220db30ff");