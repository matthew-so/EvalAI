# Challenge configuration

Following fields are required (and can be customized) in the [`challenge_config.yml`](https://github.com/Cloud-CV/EvalAI-Starters/blob/master/challenge_config.yaml).

- **title**: Title of the challenge

- **short_description**: Short description of the challenge (preferably 140 characters max)

- **description**: Long description of the challenge (use a relative path for the HTML file, e.g. `challenge_details/description.html`)

- **evaluation_criteria**: Evaluation criteria and details of the challenge (use a relative path for the HTML file, e.g. `challenge_details/evaluation.html`)

- **terms_and_conditions**: Terms and conditions of the challenge (use a relative path for the HTML file, e.g. `challenge_details/tnc.html`)

- **image**: Logo of the challenge (use a relative path for the logo in the zip configuration, e.g. `images/logo/challenge_logo.jpg`). **Note**: The image must be in jpg, jpeg or png format.

- **submission_guidelines**: Submission guidelines of the challenge (use a relative path for the HTML file, e.g. `challenge_details/submission_guidelines.html`)

- **evaluation_script**: Python script which will decide how to evaluate submissions in different phases (path of the evaluation script file or folder relative to this YAML file. For e.g. `evaluation_script/`)

- **remote_evaluation**: True/False (specify whether evaluation will happen on a remote machine or not. Default is `False`)

- **is_docker_based**: True/False (specify whether challenge uses Docker to host challenge scripts. Default is `True`)

- **start_date**: Start DateTime of the challenge (Format: YYYY-MM-DD HH:MM:SS, e.g. 2017-07-07 10:10:10) in `UTC` time zone

- **end_date**: End DateTime of the challenge (Format: YYYY-MM-DD HH:MM:SS, e.g. 2017-07-07 10:10:10) in `UTC` time zone

- **published**: True/False (Boolean field that gives the flexibility to publish the challenge once approved by EvalAI admin. Default is `False`)

- **allowed_email_domains**: A list of domains allowed to participate in the challenge. Leave blank if everyone is allowed to participate. (e.g. `["domain1.com", "domain2.org", "domain3.in"]` Participants with these email domains will only be allowed to participate.)

- **blocked_emails_domains**: A list of domains not allowed to participate in the challenge. Leave blank if everyone is allowed to participate. (e.g. `["domain1.com", "domain2.org", "domain3.in"]` Participants with these email domains will not be allowed to participate.)

- **banned_email_ids**: A list of email addresses whose teams are banned from competing in the challenge. Leave blank if everyone is allowed to participate. (e.g. teams containing at least one participant with one of these emails would not be allowed to participate: `["banneduser1@banned.edu", "banned_user2@banned.edu"]`)

- **leaderboard**:
  A leaderboard for a challenge on EvalAI consists of following subfields:

  - **id**: Unique positive integer field for each leaderboard entry

  - **schema**: Schema field contains the information about the rows of the leaderboard. A schema contains two keys in the leaderboard:

    1. `labels`: Labels are the header rows in the leaderboard according to which the challenge ranking is done.

    2. `default_order_by`: This key decides the default sorting of the leaderboard based on one of the labels defined above.

  The leaderboard schema for the [sample challenge configuration](https://github.com/Cloud-CV/EvalAI-Starters/blob/master/challenge_config.yaml) looks like this:

  ```yaml
  leaderboard:
    - id: 1
      schema:
        {
          "labels": ["Metric1", "Metric2", "Metric3", "Total"],
          "default_order_by": "Total",
        }
  ```

  The above leaderboard schema will look something like this on leaderboard UI:

  ![](_static/img/leaderboard.png "Random Number Generator Challenge - Leaderboard")

- **queue**:
  SQS queue name (blank by default).

- **aws_account_id**, **aws_access_key_id**, **aws_secret_access_key**, **aws_region**:
  AWS authentication information to be used by evaluation scripts.

- **aws_region**:
  AWS region where evaluations will be run. `us-east-1` by default.

- **task_def_arn**, **vpc_cidr**, **subnet_1_cidr**, **subnet_2_cidr**:
  The task definition ARN and VPC and subnet CIDRs for code upload challenge.

The following fields have default values but can be updated if needed.

- **is_static_dataset_code_upload**:
  True/False (specify whether challenge is a static code upload challenge. Default is `False`)

- **max_docker_image_size**:
  Maximum image size of Docker containers used to host challenge (in bytes, default is 40 GiB)

- **max_concurrent_submission_evaluation**:
  Maximum number of submissions that will be run concurrently by evaluation setup (default 100000)

- **use_host_credentials**:
  True/False (specify whether challenge will use the host's AWS credentials to run evaluations, default is `False`)

- **cli_version**:
  The CLI version used by the challenge. `evalai-cli version` by default.

- **workers**:
  True/False (specify how many active workers the challenge's Fargate will use at a time)

- **slack_webhook_url**:
  (optional) The Slack webhook that can be used to notify when a submission has been evaluated.

- **github_repository**:
  The GitHub repository where the challenge's source code can be found. Format: account_name/repository_name

- **worker_cpu_cores**:
  The amount of CPU time (in 1/1024's of a vCPU core) that the challenge will require on AWS. Maximum of 1 vCPU core (1024) is permitted. Default is 512, or 0.5 vCPUs. See [the AWS docs](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html) for the list of valid CPU and memory values.

- **worker_memory**:
  The amount of memory (in MiB) that each challenge worker will require on AWS. Default is 1024 MiB. Maximum of 2 GB is permitted. See [the AWS docs](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html) for the list of valid CPU and memory values.

- **inform_hosts**:
  True/False (specifies whether host will receive messages whenever workers are created, updated, or deleted. Default is `True`).

- **worker_instance_type**:
  Evaluation instance config for code upload challenge. Default is `g4dn.xlarge`.

- **worker_ami_type**:
  Evaluation AMI config for code upload challenge. Default is `AL2_x86_64_GPU`.

- **worker_disk_size**:
  Evaluation disk size config for code upload challenge. Default is 100 GB.

- **max_worker_instance**, **min_worker_instance**, **desired_worker_instances**:
  Maximum, minimum, and desired number of challenge worker instances. Default is max: 10, min: 1, and desired: 1.

- **cpu_only_jobs**:
  True/False (specifies whether jobs will run on the CPU only. Default is `False`).

- **job_cpu_cores**, **job_memory**:
  The number of vCPU for a code upload submission kubernetes job. Default value is 2 vCPUs and 8 GiB.

* **challenge_phases**:

  There can be multiple [challenge phases](https://evalai.readthedocs.io/en/latest/glossary.html#challenge-phase) in a challenge. A challenge phase in a challenge contains the following subfields:

  - **id**: Unique integer identifier for the challenge phase

  - **name**: Name of the challenge phase

  - **description**: Long description of the challenge phase (set the relative path of the HTML file, e.g. `challenge_details/phase1_description.html`)

  - **leaderboard_public**: True/False (a Boolean field that gives the flexibility to Challenge Hosts to either make the leaderboard public or private. Default is `False`)

  - **is_public**: True/False (a Boolean field that gives the flexibility to Challenge Hosts to either hide or show the challenge phase to participants. Default is `False`)

  - **is_submission_public**: True/False (a Boolean field that gives the flexibility to Challenge Hosts to either make the submissions by default public/private. Note that this will only work when the `leaderboard_public` property is set to true. Default is `False`)

  - **start_date**: Start DateTime of the challenge phase (Format: YYYY-MM-DD HH:MM:SS, e.g. 2017-07-07 10:10:10)

  - **end_date**: End DateTime of the challenge phase (Format: YYYY-MM-DD HH:MM:SS, e.g. 2017-07-07 10:10:10)

  - **test_annotation_file**: This file is used for ranking the submission made by a participant. An annotation file can be shared by more than one challenge phase. (Path of the test annotation file relative to this YAML file, e.g. `challenge_details/test_annotation.txt`)

  - **codename**: Unique id for each challenge phase. Note that the codename of a challenge phase is used to map the results returned by the evaluation script to a particular challenge phase. The codename specified here should match with the codename specified in the evaluation script to perfect mapping.

  - **max_submissions_per_day**: Positive integer which tells the maximum number of submissions per day to a challenge phase.

  - **max_submissions_per_month**: Positive integer which tells the maximum number of submissions per month to a challenge phase.

  - **max_submissions**: a Positive integer that decides the overall maximum number of submissions that can be done to a challenge phase.

- **dataset_splits**:

  Dataset splits define the subset of test-set on which the submissions will be evaluated on. Generally, most challenges have two splits:

  1. **test-dev** (Allow participants to make large number of submissions, let them see how they are doing, and let them overfit)
  2. **test-challenge** (Allow small number of submissions so that they cannot mimic test-set. Use this split to decide the winners for the challenge)

  A dataset split has the following subfields:

  - **id**: Unique integer identifier for the split

  - **name**: Name of the split (it must be unique for every split)

  - **codename**: Unique id for each split. Note that the codename of a dataset split is used to map the results returned by the evaluation script to a particular dataset split in EvalAI's database. Please make sure that no two dataset splits have the same codename. Again, make sure that the dataset split's codename match with what is in the evaluation script provided by the challenge host.

- **challenge_phase_splits**:

  A challenge phase split is a relation between a challenge phase and dataset splits for a challenge (many to many relation). This is used to set the privacy of submissions (public/private) to different dataset splits for different challenge phases.

  - **challenge_phase_id**: Id of `challenge_phase` to map with

  - **leaderboard_id**: Id of `leaderboard`

  - **dataset_split_id**: Id of `dataset_split`

  - **visibility**: It will set the visibility of the numbers corresponding to metrics for this `challenge_phase_split`. Select one of the following positive integers based on the visibility level you want:

  - **leaderboard_decimal_precision**: Positive integer field used for varying the leaderboard decimal precision. Default value is `2`.

  - **is_leaderboard_order_descending**: True/False (a Boolean field that gives the flexibility to challenge host to change the default leaderboard sorting order. It is useful in cases where you have error as a metric and want to sort the leaderboard in increasing order of error value. Default is `True`)

  | Visibility | Description                                                             |
  | ---------- | ----------------------------------------------------------------------- |
  | 1          | Only visible to challenge host                                          |
  | 2          | Only visible to challenge host and participant who made that submission |
  | 3          | Visible to everyone on leaderboard                                      |
