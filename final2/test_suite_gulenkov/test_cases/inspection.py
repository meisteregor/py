from test_cases import unix_commands


class Inspection(object):
    """Tying test cases to make the run verbose. Arguments step and response are quite similar logically"""

    @staticmethod
    def is_nfs_restarted(response, class_name):
        if not response:
            class_name.logger.info("Restarting nfs....")
            class_name.logger.debug("* SUCCESS")
        else:
            class_name.logger.error(response)

    @staticmethod
    def is_rpcbind_restarted(response, class_name):
        if not response:
            class_name.logger.info("Restarting rpcbind....")
            class_name.logger.debug("* SUCCESS")
        else:
            class_name.logger.error(response)

    @staticmethod
    def is_fw_disabled(response, class_name):
        if not response:
            class_name.logger.info("Disabling firewalls....")
            class_name.logger.debug("* SUCCESS")
        else:
            class_name.logger.error(response)

    @staticmethod
    def is_fw_stopped(response, class_name):
        if not response:
            class_name.logger.info("Stopping firewalls....")
            class_name.logger.debug("* SUCCESS")
        else:
            class_name.logger.error(response)

    @staticmethod
    def check_config_rewritten_successfully(response, class_name):
        if not response:
            class_name.logger.debug("prepare server's config for mounting: *SUCCESS ")
        else:
            class_name.logger.error(response)

    @staticmethod
    def check_if_nfs_packages_installed(response, class_name):
        if not response:
            class_name.logger.info("Getting NFS packages: *SUCCESS")
        else:
            class_name.logger.error(response)

    @staticmethod
    def is_pinging_remote(response, class_name):
        if response:
            class_name.logger.debug("* SUCCESS\n")
        else:
            class_name.logger.error(response)

    @staticmethod
    def is_pinging_local(response, class_name):
        if not response:
            class_name.logger.debug("* SUCCESS")
        else:
            class_name.logger.error(response)

    @staticmethod
    def is_mounted(response, class_name):
        if not response:
            class_name.logger.info("NFS mount: *SUCCESS\n")
        else:
            class_name.logger.error(response)

    @staticmethod
    def check_local_dir(response, class_name):
        if not response:
            class_name.logger.debug("Local dir for mount: READY")
        else:
            class_name.logger.error(response)

    @staticmethod
    def check_remote_dir(response, class_name):
        if not response:
            class_name.logger.debug("Remote dir for mount: READY")
        else:
            class_name.logger.error(response)

    @staticmethod
    def check_change_dir(step, class_name, number_of_step):
        if not step:
            class_name.logger.info("Step %d is PASSED" % number_of_step)
            class_name.logger.debug("You changed a directory")
        else:
            class_name.logger.info("Step %d is FAILED" % number_of_step)
            class_name.logger.error(step)

    @staticmethod
    def check_work_dir(class_name):
        class_name.logger.debug(unix_commands.UnixCommands.pwd())

    @staticmethod
    def check_touch_file(step, class_name, number_of_step):
        if not step:
            class_name.logger.info("Step %d is PASSED" % number_of_step)
            class_name.logger.debug("A file has been created ")
        else:
            class_name.logger.info("Step %d is FAILED" % number_of_step)
            class_name.logger.error(step)

    @staticmethod
    def check_list_of_files(class_name):
        class_name.logger.debug(unix_commands.UnixCommands.ls())

    @staticmethod
    def check_cat_file(step, class_name, number_of_step):
        if not step:
            class_name.logger.info("Step %d is PASSED" % number_of_step)
            class_name.logger.debug("You look through a file via cat ")
        else:
            class_name.logger.info("Step %d is FAILED" % number_of_step)
            class_name.logger.error(step)

    @staticmethod
    def check_ssh_to_server(step, class_name, number_of_step):
        if not step:
            class_name.logger.info("Step %d is PASSED" % number_of_step)
            class_name.logger.debug("Remote command has been SUCCESSFUL")
        else:
            class_name.logger.info("Step %d is FAILED" % number_of_step)
            class_name.logger.error(step)

    @staticmethod
    def check_make_dir(step, class_name, number_of_step):
        if not step:
            class_name.logger.info("Step %d is PASSED" % number_of_step)
            class_name.logger.debug("The directory has been created ")
        else:
            class_name.logger.info("Step %d is FAILED" % number_of_step)
            class_name.logger.error(step)

    @staticmethod
    def check_copy(step, class_name, number_of_step):
        if not step:
            class_name.logger.info("Step %d is PASSED" % number_of_step)
            class_name.logger.debug("The file was copied ")
        else:
            class_name.logger.info("Step %d is FAILED" % number_of_step)
            class_name.logger.error(step)

    @staticmethod
    def check_rename(step, class_name, number_of_step):
        if not step:
            class_name.logger.info("Step %d is PASSED" % number_of_step)
            class_name.logger.debug("The file was renamed")
        else:
            class_name.logger.info("Step %d is FAILED" % number_of_step)
            class_name.logger.error(step)

    @staticmethod
    def check_remove(step, class_name, number_of_step):
        if not step:
            class_name.logger.info("Step %d is PASSED" % number_of_step)
            class_name.logger.debug("The file was removed")
        else:
            class_name.logger.info("Step %d is FAILED" % number_of_step)
            class_name.logger.error(step)

    @staticmethod
    def check_move(step, class_name, number_of_step):
        if not step:
            class_name.logger.info("Step %d is PASSED" % number_of_step)
            class_name.logger.debug("The file was moved ")
        else:
            class_name.logger.info("Step %d is FAILED" % number_of_step)
            class_name.logger.error(step)

    @staticmethod
    def check_write_into_file(step, class_name, number_of_step):
        if not step:
            class_name.logger.info("Step %d is PASSED" % number_of_step)
            class_name.logger.debug("Record data into the file has been completed successfully")
        else:
            class_name.logger.info("Step %d is FAILED" % number_of_step)
            class_name.logger.error(step)

    @staticmethod
    def check_read_from_file(class_name, file_name):
        class_name.logger.debug('Data inside file is {}'.format(unix_commands.UnixCommands.read_from_file(file_name)))

    @staticmethod
    def check_run_script(step, class_name, number_of_step):
        if not step:
            class_name.logger.info("Step %d is PASSED" % number_of_step)
            class_name.logger.debug("The file was executed successfully")
        else:
            class_name.logger.info("Step %d is FAILED" % number_of_step)
            class_name.logger.error(step)
