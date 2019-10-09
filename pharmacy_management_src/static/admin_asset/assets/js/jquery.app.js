! function(t) {
	
	var i = function() {
		this.$body = t("body"), this.$sideBar = t("aside.left-panel"), this.$navbarToggle = t(".navbar-toggle"), this.$navbarItem = t("aside.left-panel nav.navigation > ul > li:has(ul) > a")
	};
	i.prototype.init = function() {
		var i = this;
		t(document).on("click", ".navbar-toggle", function() {
			i.$sideBar.toggleClass("collapsed")
			$(".nav-text").toggle();
		}), this.$navbarItem.click(function() {
			return 0 == i.$sideBar.hasClass("collapsed") || t(window).width() < 768 ? (t("aside.left-panel nav.navigation > ul > li > ul").slideUp(300), t("aside.left-panel nav.navigation > ul > li").removeClass("active"), t(this).next().is(":visible") || (t(this).next().slideToggle(300, function() {
				t("aside.left-panel:not(.collapsed)").getNiceScroll().resize()
			}), t(this).closest("li").addClass("active")), !1) :
			void 0
		}), t.isFunction(t.fn.niceScroll) && t("aside.left-panel:not(.collapsed)").niceScroll({
			cursorcolor : "#8e909a",
			cursorborder : "0px solid #fff",
			cursoropacitymax : "0.5",
			cursorborderradius : "0px"
		})
	}, t.SideBar = new i, t.SideBar.Constructor =
	i
}(window.jQuery), function(t) {
	
	var i = function() {
		this.$body = t("body"), this.$portletIdentifier = ".portlet", this.$portletCloser = '.portlet a[data-toggle="remove"]', this.$portletRefresher = '.portlet a[data-toggle="reload"]'
	};
	i.prototype.init = function() {
		var i = this;
		t(document).on("click", this.$portletCloser, function(o) {
			o.preventDefault();
			var e = t(this).closest(i.$portletIdentifier),
			    n = e.parent();
			e.remove(), 0 == n.children().length && n.remove()
		}), t(document).on("click", this.$portletRefresher, function(o) {
			o.preventDefault();
			var e = t(this).closest(i.$portletIdentifier);
			e.append('<div class="panel-disabled"><div class="loader-1"></div></div>');
			var n = e.find(".panel-disabled");
			setTimeout(function() {
				n.fadeOut("fast", function() {
					n.remove()
				})
			}, 500 + 1500 * Math.random())
		})
	}, t.Portlet = new i, t.Portlet.Constructor =
	i
}(window.jQuery), function(t) {
	
	var i = function() {
		this.VERSION = "1.0.0", this.AUTHOR = "Coderthemes", this.SUPPORT = "coderthemes@gmail.com", this.pageScrollElement = "html, body", this.$body = t("body")
	};
	i.prototype.initTooltipPlugin = function() {
		t.fn.tooltip && t('[data-toggle="tooltip"]').tooltip()
	}, i.prototype.initPopoverPlugin = function() {
		t.fn.popover && t('[data-toggle="popover"]').popover()
	}, i.prototype.initNiceScrollPlugin = function() {
		t.fn.niceScroll && t(".nicescroll").niceScroll({
			cursorcolor : "#9d9ea5",
			cursorborderradius : "0px"
		})
	}, i.prototype.initKnob = function() {
		t(".knob").length > 0 && t(".knob").knob()
	}, i.prototype.init = function() {
		this.initTooltipPlugin(), this.initPopoverPlugin(), this.initNiceScrollPlugin(), this.initKnob(), t.SideBar.init(), t.Portlet.init()
	}, t.AdminaApp = new i, t.AdminaApp.Constructor =
	i
}(window.jQuery), function(t) {
	
	t.AdminaApp.init()
}(window.jQuery);
var wow = new WOW({
	boxClass : "wow",
	animateClass : "animated",
	offset : 50,
	mobile : !1
});
wow.init(); 