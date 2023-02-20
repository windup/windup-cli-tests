MIGRATION_ISSUES_DETAILS["3c8bbc28-04c4-4ba6-804b-7ebf4da37b1b"] = [
{description: "<p>Replace the <code>spring-boot-maven-plugin<\/code> dependency. The <code>spring-boot-maven-plugin<\/code> dependency needs to be replaced with <code>quarkus-maven-plugin<\/code>, so that the application is built with Quarkus, both for running on the JVM and in native mode.<\/p>", ruleID: "springboot-plugins-to-quarkus-0000", issueName: "Replace the spring-boot-maven-plugin dependency",
problemSummaryID: "3c8bbc28-04c4-4ba6-804b-7ebf4da37b1b", files: [
{l:"<a class='' href='pom_xml.html?project=4423800'>META-INF/maven/com.rmarting.kafka/kafka-clients-sb-sample/pom.xml<\/a>", oc:"1"},
], resourceLinks: [
{h:"https://quarkus.io/guides/maven-tooling#build-tool-maven", t:"Building Quarkus with maven"},
]},
];
onProblemSummaryLoaded("3c8bbc28-04c4-4ba6-804b-7ebf4da37b1b");